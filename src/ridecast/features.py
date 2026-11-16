"""Feature engineering for the zone-by-hour table.

Session 5. Concepts: pandas groupby + shift, datetime accessors, and avoiding
leakage (a feature may only use information available before the hour it predicts).
"""

from collections.abc import Sequence

import pandas as pd


def add_calendar_features(df: pd.DataFrame, time_col: str = "hour") -> pd.DataFrame:
    """Add hour_of_day (0-23), day_of_week (0=Monday), is_weekend.

    Return a new DataFrame; don't modify the input in place.
    """
    raise NotImplementedError("Session 5")


def add_lag_features(
    df: pd.DataFrame,
    lags: Sequence[int] = (1, 2, 3, 24, 168),
    target_col: str = "trips",
) -> pd.DataFrame:
    """Add trips_lag_<k> columns: the target k hours earlier, in the same zone.

    Implement with groupby("zone_id")[target_col].shift(k) on data sorted by
    zone_id, hour. The dense grid from aggregate.py is what makes "shift by k rows"
    equal "k hours ago".

    The first max(lags) hours of each zone have no history, so their lags are NaN.
    Decide in Session 5 whether to drop those rows (simplest) or keep them.
    """
    raise NotImplementedError("Session 5")


def add_rolling_features(
    df: pd.DataFrame,
    windows: Sequence[int] = (24, 168),
    target_col: str = "trips",
) -> pd.DataFrame:
    """Add trips_rollmean_<w>: mean of the previous w hours in the same zone.

    Leakage trap: shift by 1 before rolling, so the window ends at hour t-1 and
    never includes the hour being predicted.
    """
    raise NotImplementedError("Session 5")
