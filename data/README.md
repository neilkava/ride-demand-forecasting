# data/

Nothing in `raw/` or `processed/` is committed to git (see `.gitignore`).

- `raw/`: monthly files exactly as downloaded, for example `fhvhv_tripdata_2026-06.parquet`, plus `taxi_zone_lookup.csv`. Never edit these.
- `processed/`: tables built by our code, for example `zone_hour.parquet`. Safe to delete and rebuild.

Source: NYC TLC Trip Record Data, High Volume For-Hire Vehicle records.
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
