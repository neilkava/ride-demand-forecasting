"""Forecast error metrics.

Session 4. The tests in tests/test_metrics.py already describe the expected
behaviour: implement these until `uv run pytest tests/test_metrics.py` passes.

Why not MAPE (mean absolute percentage error)? It divides each error by the actual
value, and many zone-hours have 0 trips, so it is undefined or explodes.
"""

from numpy.typing import ArrayLike


def mae(y_true: ArrayLike, y_pred: ArrayLike) -> float:
    """Mean absolute error: average of |actual - predicted|. Units: trips."""
    raise NotImplementedError("Session 4")


def wape(y_true: ArrayLike, y_pred: ArrayLike) -> float:
    """Weighted absolute percentage error: sum(|actual - predicted|) / sum(|actual|).

    Returns a fraction (0.25 means the total error is 25% of total trips).
    Raise ValueError if sum(|actual|) is 0.
    """
    raise NotImplementedError("Session 4")
