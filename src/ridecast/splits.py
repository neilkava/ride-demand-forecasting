"""Time-based train / validation / test split.

Session 4. Time series are never split randomly: a random split lets the model
train on Tuesday 3 p.m. and get tested on Tuesday 2 p.m., which leaks the answer.
Train on the past, validate on the next block, test on the final block.
"""

import pandas as pd


def time_split(
    df: pd.DataFrame,
    val_start: pd.Timestamp,
    test_start: pd.Timestamp,
    time_col: str = "hour",
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split by timestamp into (train, validation, test).

    train:       time_col <  val_start
    validation:  val_start <= time_col < test_start
    test:        time_col >= test_start

    Raise ValueError if val_start >= test_start or if any split comes out empty.
    """
    raise NotImplementedError("Session 4")
