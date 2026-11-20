"""LightGBM baseline on calendar and lag features.

Session 5. Concepts: gradient-boosted trees, early stopping on the validation
set, categorical features, feature importance.
"""

import lightgbm as lgb
import pandas as pd


def train(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
) -> lgb.LGBMRegressor:
    """Fit an LGBMRegressor with early stopping on the validation set.

    Starting points to try (tune on validation, never on test):
        - objective "poisson" (the target is a count) vs. the default "regression"
        - zone_id as a categorical feature
        - n_estimators high (for example 2000) with lgb.early_stopping(50)
    """
    raise NotImplementedError("Session 5")
