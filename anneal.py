"""Useful miscellaneous functions."""
from typing import Callable


def get_linear_anneal_func(
    start_value: float, end_value: float, start_step: int, end_step: int
) -> Callable:
    """Create a linear annealing function.

    Parameters
    ----------
    start_value : float
        Initial value for linear annealing.
    end_value : float
        Terminal value for linear annealing.
    start_step : int
        Step to start linear annealing.
    end_step : int
        Step to end linear annealing.

    Returns
    -------
    linear_anneal_func : Callable
        A function that returns annealed value given a step index.

    """

    def linear_anneal_func(step):
        if step <= start_step:
            return start_value
        if step >= end_step:
            return end_value

        # Formula for line when two points are known:
        #             y1 - y0
        #   y - y0 = --------- (x - x0)
        #             x1 - x0
        return (end_value - start_value) / (end_step - start_step) * (
            step - start_step
        ) + start_value

    return linear_anneal_func
