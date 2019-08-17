"""Ensure reproducibility."""
import random


def set_global_random_seeds(seed, use_numpy=False, use_torch=False):
    """Set random seeds for modules and packages to ensure reproducibility."""
    random.seed(seed)

    if use_numpy:
        import numpy as np

        np.random.seed(seed)
    if use_torch:
        import torch

        torch.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
