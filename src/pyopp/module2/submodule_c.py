import numpy as np


def lin_fit(
    x: np.ndarray | float,
    a: float,
    b: float
) -> np.ndarray | float:
    """Linear fit function.

    Parameters
    ----------
    x : np.ndarray or float
        Array of x-positions.
    a : float
        Slope of the function.
    b : float
        y-intercept of the function.

    Returns
    -------
    np.ndarray or float
        Resulting y-values.
    """
    return a * x + b


def exp_fit(
    x: np.ndarray | float,
    a: float,
    b: float,
    c: float,
) -> np.ndarray | float:
    """Exponential fit function.

    Parameters
    ----------
    x : np.ndarray
        Array of x-positions.
    a : float
        Scale of the function.
    b : float
        Strength of growth or decay.
    c : float
        y-intercept of the function.

    Returns
    -------
    np.ndarray or float
        Resulting y-values.
    """
    return a * np.exp(-b * x) + c
