"""Save and load trained PyTorch models.

A directory is given for save since multiple models
can be saved in one run, but a path (including filname)
is given for load since only one model is loaded.
"""
import os

import torch

from .timestamp import get_timestamp


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


def save_models(save_dir: str, suffix: str = "net", **kwargs):
    """Save specified models.

    Parameters
    ----------
    save_dir : str
        Save directory, not excluding the filename.
    suffix : str
        Savefile suffix after timestamp.

    Returns
    -------
    unique_save_dir : str
        The unique directory with timestamp, generated
        inside the specified save directory.

    """
    # Create specified directory if it does not exist yet
    unique_save_dir = save_dir + f"/{get_timestamp()}/"
    unique_save_path = save_dir + f"/{get_timestamp()}/{suffix}.pt"
    if not os.path.exists(unique_save_dir):
        os.makedirs(unique_save_dir)

    torch.save(
        {key: value.state_dict() for key, value in kwargs.items()}, unique_save_path
    )
    return unique_save_dir
