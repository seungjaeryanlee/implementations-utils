"""Save and load trained PyTorch models.

A directory is given for save since multiple models
can be saved in one run, but a path (including filname)
is given for load since only one model is loaded.
"""
import os

import torch


def load_models(load_path: str, **kwargs):
    """Load specified models.

    Parameters
    ----------
    load_path : str
        Load path including the filename.

    """
    state_dict = torch.load(load_path)
    for key, value in kwargs.items():
        value.load_state_dict(state_dict[key])


def save_models(save_dir: str, filename: str = "net", **kwargs):
    """Save specified models.

    Parameters
    ----------
    save_dir : str
        Save directory, not excluding the filename.
    filename : str
        Save filename.

    """
    # Create specified directory if it does not exist yet
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    torch.save(
        {key: value.state_dict() for key, value in kwargs.items()},
        f"{save_dir}/{filename}.pt",
    )
