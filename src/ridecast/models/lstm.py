"""PyTorch LSTM: read the past week of demand for a zone, predict the next hour.

Sessions 6 and 7. Concepts: tensors and shapes, sliding windows, scaling fitted on
the training period only, nn.Module, Dataset/DataLoader, writing the training loop
by hand (forward, loss, backward, optimizer step), early stopping, devices (CPU vs.
Apple's MPS GPU), saving and loading a state_dict.

Only this module imports torch, so the rest of the package and the tests load
without it.

Shapes used throughout (batch_first=True):
    X: (batch, window, n_features)   e.g. (256, 168, 1)
    y: (batch,)
"""

from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader

from ridecast.config import SEASON_LENGTH


def get_device() -> torch.device:
    """Return torch.device("mps") if Apple's GPU backend is available, else "cpu".

    Training on the Mac can use MPS. The API container (Docker, Fargate, kind) has
    no Apple GPU, so serving always ends up on "cpu"; that is why the fallback matters.
    Session 6: also time one epoch on each device. For a model this small, MPS
    is not guaranteed to be faster, and measuring that is the point.
    """
    raise NotImplementedError("Session 6")


def make_windows(
    series: np.ndarray,
    window: int = SEASON_LENGTH,
) -> tuple[np.ndarray, np.ndarray]:
    """Slice one zone's hourly series into supervised examples.

    Args:
        series: 1-D array of hourly trips for one zone, in time order.
        window: number of past hours the model sees.

    Returns:
        X with shape (n_examples, window, 1) and y with shape (n_examples,),
        both float32, where X[i] is series[i : i + window] and y[i] is series[i + window].

    float32 matters: NumPy defaults to float64, PyTorch models use float32, and MPS
    does not support float64 at all.

    Session 6 exercise: write this with a plain loop first, check the shapes by
    hand on a 10-element array, then replace the loop with
    numpy.lib.stride_tricks.sliding_window_view.
    """
    raise NotImplementedError("Session 6")


def make_loader(
    X: np.ndarray,
    y: np.ndarray,
    batch_size: int = 256,
    shuffle: bool = False,
) -> DataLoader:
    """Wrap X and y in a TensorDataset and return a DataLoader that yields batches.

    Use shuffle=True for training and shuffle=False for validation and test.
    Shuffling training *windows* is fine. Each window is a complete example and
    the split is already done by time. "Never shuffle" is about the split, not
    the batch order.
    """
    raise NotImplementedError("Session 6")


class LSTMForecaster(nn.Module):
    """nn.LSTM(n_features -> hidden_size, batch_first=True) followed by nn.Linear(hidden_size -> 1).

    forward(x): x has shape (batch, window, n_features). Run the LSTM, take the
    output at the last time step, shape (batch, hidden_size), apply the Linear
    layer, and squeeze to shape (batch,).

    Later experiments (Session 7): extra input channels (hour of day, day of week),
    a zone embedding (nn.Embedding), a second LSTM layer, Poisson loss
    (nn.PoissonNLLLoss).
    """

    def __init__(self, n_features: int = 1, hidden_size: int = 64):
        super().__init__()
        raise NotImplementedError("Session 6")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("Session 6")


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> float:
    """One pass over the training data; return the mean loss.

    For each batch: move it to device, optimizer.zero_grad(), forward pass, loss,
    loss.backward(), optimizer.step(). Call model.train() first.
    """
    raise NotImplementedError("Session 6")


def evaluate(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    device: torch.device,
) -> float:
    """Mean loss over a loader with no weight updates.

    Call model.eval() and run inside torch.no_grad(): no gradients and no
    optimizer step.
    """
    raise NotImplementedError("Session 6")


def train(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    epochs: int = 20,
    lr: float = 1e-3,
    patience: int = 3,
    device: torch.device | None = None,
) -> dict[str, list[float]]:
    """Full training run with early stopping; return {"train_loss": [...], "val_loss": [...]}.

    Loss nn.L1Loss() (MAE) to start, optimizer torch.optim.Adam. After each epoch,
    evaluate on validation. Keep a copy of the best state_dict, and stop when
    validation loss has not improved for `patience` epochs. Load the best weights
    back before returning. This is what Keras's EarlyStopping(restore_best_weights=True)
    does for you; here you write it yourself.
    """
    raise NotImplementedError("Session 7")


def save_model(model: nn.Module, path: Path) -> None:
    """Save model.state_dict() (the learned weights only) to a .pt file."""
    raise NotImplementedError("Session 7")


def load_model(path: Path, n_features: int = 1, hidden_size: int = 64) -> LSTMForecaster:
    """Rebuild LSTMForecaster, then load the weights with map_location="cpu".

    Call .eval() on it before returning. map_location="cpu" lets a model trained on
    MPS load in the CPU-only API container.
    """
    raise NotImplementedError("Session 7")
