"""Download monthly HVFHV trip files and the zone lookup table into data/raw/.

Run from the repository root:
    uv run python -m ridecast.data.download 2026-06 2026-07 2026-08

Session 1. Concepts you will practice: pathlib, f-strings, argparse, streaming a
large download to disk, making a script safe to run twice (idempotent).
"""

from pathlib import Path

from ridecast.config import RAW_DIR


def download_month(month: str, dest_dir: Path = RAW_DIR) -> Path:
    """Download one month of trip data and return the local file path.

    Args:
        month: "YYYY-MM", for example "2026-06".
        dest_dir: folder to save into. Create it if it doesn't exist.

    Behaviour to implement:
        1. Build the URL from config.TRIP_DATA_URL.
        2. If the file already exists locally, print a message and return its path
           without downloading again.
        3. Otherwise download it. Files are about 450-500 MB, so stream to disk
           instead of reading the whole response into memory.
           (Standard library: urllib.request.urlretrieve, or urlopen + shutil.copyfileobj.)
        4. Download to a temporary name such as "<file>.part" and rename when done,
           so an interrupted download never looks like a finished file.
    """
    raise NotImplementedError("Session 1")


def download_zone_lookup(dest_dir: Path = RAW_DIR) -> Path:
    """Download taxi_zone_lookup.csv (LocationID, Borough, Zone, service_zone)."""
    raise NotImplementedError("Session 1")


def main() -> None:
    """Parse month arguments from the command line and download each one.

    Use argparse with nargs="*" and fall back to config.DEFAULT_MONTHS.
    """
    raise NotImplementedError("Session 1")


if __name__ == "__main__":
    main()
