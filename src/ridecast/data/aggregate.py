"""Turn raw trip files into one small table: Lyft trips per zone per hour.

Run from the repository root:
    uv run python -m ridecast.data.aggregate

Session 2. Concepts: DuckDB querying Parquet on disk, GROUP BY, date_trunc,
building a complete grid with CROSS JOIN, LEFT JOIN + COALESCE to fill zeros.

Output: data/processed/zone_hour.parquet with columns
    zone_id (int)        TLC taxi zone, from PULocationID
    hour    (timestamp)  start of the hour, from request_datetime
    trips   (int)        number of Lyft trips requested in that zone and hour, 0 if none
"""

from collections.abc import Sequence
from pathlib import Path

import pandas as pd

from ridecast.config import DEFAULT_MONTHS, RAW_DIR


def build_zone_hour_table(
    months: Sequence[str] = DEFAULT_MONTHS,
    raw_dir: Path = RAW_DIR,
) -> pd.DataFrame:
    """Aggregate raw trips to a dense zone-by-hour table.

    Steps to implement (one DuckDB query, or a few small ones):
        1. Read the monthly files with read_parquet. Select only the columns you
           need; DuckDB then skips the rest of the file.
        2. Keep rows where hvfhs_license_num = config.LYFT_LICENSE.
        3. Bucket request_datetime to the hour with date_trunc and count trips per
           (PULocationID, hour).
        4. Keep only hours inside the requested months. A few trips in each file
           have a request time just before the month starts.
        5. Build the full grid: every zone that appears x every hour in the range
           (generate_series for the hours, CROSS JOIN with the zones).
        6. LEFT JOIN the counts onto the grid and COALESCE missing counts to 0.
        7. Return as a pandas DataFrame sorted by zone_id, hour.

    Decisions to make in Session 2 and record in the context file:
        - Zones 264 and 265 mean "unknown" and "outside NYC". Drop them?
        - Why request_datetime and not pickup_datetime? (Demand happens when the
          rider asks, not when the car arrives.)

    Sanity checks to add as tests:
        - rows == number of zones * number of hours
        - no nulls, no negative counts
        - sum(trips) equals a plain COUNT(*) of Lyft rows over the same period
    """
    raise NotImplementedError("Session 2")


def main() -> None:
    """Build the table and write it to config.ZONE_HOUR_PATH."""
    raise NotImplementedError("Session 2")


if __name__ == "__main__":
    main()
