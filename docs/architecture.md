# Architecture

GitHub renders these diagrams. In VS Code, install the "Markdown Preview Mermaid Support" extension.

## 1. Training pipeline (Phase 1)

```mermaid
flowchart TD
    A["TLC HVFHV Parquet files<br/>one per month, all companies"] -->|download.py| B["data/raw/"]
    B -->|"aggregate.py (DuckDB SQL)<br/>keep hvfhs_license_num = HV0005<br/>bucket request_datetime by hour<br/>count trips per zone"| C["Sparse counts<br/>(only zone-hours that had trips)"]
    C -->|"join onto every zone x every hour<br/>fill missing with 0"| D["data/processed/zone_hour.parquet<br/>columns: zone_id, hour, trips"]
    D -->|splits.py| E["train | validation | test<br/>split by time, never shuffled"]
    E -->|features.py| F["calendar + lag features"]
    F --> G1["Seasonal naive<br/>trips at same hour last week"]
    F --> G2["LightGBM"]
    F --> G3["Keras LSTM<br/>past 168 hours -> next hour"]
    G1 & G2 & G3 -->|metrics.py| H["WAPE and MAE on the test period"]
```

Why the zero-fill step matters: a zone with no trips at 4 a.m. has no row in the raw
data. Without the fill, the model never sees a zero, lag features point at the wrong
hour, and the error metrics skip the quiet hours.

## 2. Serving and deployment (Phases 2 and 3)

```mermaid
flowchart LR
    T["Training script"] -->|upload model file| S3[("S3 bucket")]
    subgraph Container["Docker image"]
        API["FastAPI app<br/>/health, /predict"]
    end
    S3 -->|download at startup| API
    Client["Postman / curl"] -->|"POST /predict<br/>zone_id, hour"| API
    API -->|forecast| Client
    Container -.->|push| ECR["ECR"]
    ECR -.->|run| ECS["ECS Fargate"]
    Container -.->|same image| K8s["kind (local Kubernetes)"]
```

The model file lives in S3, not inside the image, so a retrained model ships without
rebuilding the container.

## 3. Why a rider-level A/B test is biased in a marketplace (Phase 2)

```mermaid
flowchart TD
    D["Drivers in a zone<br/>(one shared pool)"]
    T["Treatment riders<br/>get a discount, request more"] -->|take more drivers| D
    C["Control riders<br/>no discount"] -->|fewer drivers left| D
    D --> R["Control completes fewer trips than it would have<br/>so treatment minus control overstates the true effect"]
```

A switchback test randomizes whole zone-and-time blocks instead of riders, so both
groups never compete for the same drivers at the same time. The cost is fewer
independent units, so the estimate is noisier.
