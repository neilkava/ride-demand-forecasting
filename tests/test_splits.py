"""Specification for splits.time_split. Fails until Session 4."""

import pandas as pd
import pytest

from ridecast.splits import time_split


@pytest.fixture
def hourly():
    hours = pd.date_range("2026-06-01", periods=10 * 24, freq="h")
    return pd.DataFrame({"zone_id": 1, "hour": hours, "trips": range(len(hours))})


def test_splits_are_ordered_and_cover_everything(hourly):
    val_start, test_start = pd.Timestamp("2026-06-07"), pd.Timestamp("2026-06-09")
    train, val, test = time_split(hourly, val_start, test_start)

    assert len(train) + len(val) + len(test) == len(hourly)
    assert train["hour"].max() < val_start
    assert val["hour"].min() == val_start
    assert val["hour"].max() < test_start
    assert test["hour"].min() == test_start


def test_rejects_boundaries_in_the_wrong_order(hourly):
    with pytest.raises(ValueError):
        time_split(hourly, pd.Timestamp("2026-06-09"), pd.Timestamp("2026-06-07"))


def test_rejects_an_empty_split(hourly):
    with pytest.raises(ValueError):
        time_split(hourly, pd.Timestamp("2026-05-01"), pd.Timestamp("2026-06-05"))
