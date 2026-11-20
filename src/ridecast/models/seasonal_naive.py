"""Seasonal-naive baseline: predict the value from the same hour one week ago.

Session 4. No training at all. Any real model has to beat this to be worth having.
"""

import pandas as pd

from ridecast.config import SEASON_LENGTH


def predict(df: pd.DataFrame, season_length: int = SEASON_LENGTH) -> pd.Series:
    """Return a Series aligned to df: trips in the same zone, season_length hours earlier.

    df has columns zone_id, hour, trips and covers a continuous period that starts
    at least season_length hours before the first hour you want to score.
    Rows without enough history get NaN; drop them before scoring.
    """
    raise NotImplementedError("Session 4")
