"""These tests are the specification for metrics.py. They fail until Session 4."""

import pytest

from ridecast.metrics import mae, wape


def test_mae_known_values():
    # absolute errors: 2, 1, 3 -> mean 2.0
    assert mae([10, 0, 10], [8, 1, 13]) == pytest.approx(2.0)


def test_wape_known_values():
    # sum of absolute errors 6, sum of actuals 20 -> 0.3
    assert wape([10, 0, 10], [8, 1, 13]) == pytest.approx(0.3)


def test_perfect_forecast_scores_zero():
    assert mae([1, 2, 3], [1, 2, 3]) == 0
    assert wape([1, 2, 3], [1, 2, 3]) == 0


def test_wape_handles_zero_actuals_inside_the_series():
    # the zero must not cause a division error; only the total matters
    assert wape([0, 4], [1, 4]) == pytest.approx(0.25)


def test_wape_rejects_all_zero_actuals():
    with pytest.raises(ValueError):
        wape([0, 0], [1, 2])
