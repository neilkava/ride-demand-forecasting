"""Paths and constants. Import from here; don't hardcode paths anywhere else."""

from pathlib import Path

# src/ridecast/config.py -> parents[2] is the repository root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

# {month} is "YYYY-MM", for example "2026-06"
TRIP_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_{month}.parquet"
ZONE_LOOKUP_URL = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

# hvfhs_license_num values: HV0002 Juno, HV0003 Uber, HV0004 Via, HV0005 Lyft
LYFT_LICENSE = "HV0005"

DEFAULT_MONTHS = ("2026-06", "2026-07", "2026-08")

# Hours in one week. Demand repeats weekly, so "same hour last week" is lag 168.
SEASON_LENGTH = 168

ZONE_HOUR_PATH = PROCESSED_DIR / "zone_hour.parquet"
