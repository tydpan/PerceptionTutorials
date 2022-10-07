import numpy as np


def afunc(array1: np.ndarray, array2: np.ndarray, mode: str = "+", pow: int = 2) -> np.ndarray:
    """Sums two matrices, then exponentiates each element by pow power.

    Args:
        array1: A numpy.ndarray.
        array2: A numpy.ndarray.
        mode: A string representing '+' or '-' matrix operations.
        pow: An integer representing the power.

    Returns:
        A numpy.ndarray matrix, summing the passed matrices and exponentiating each element by pow.
    """
    assert array1.shape == array2.shape, "size mismatch"
    assert type(pow) == int, "pow should be type int"

    if mode == "+":
        result = array1 + array2
    elif mode == "-":
        result = array1 - array2
    else:
        raise ValueError(f"mode is either '+' or '-' but got {mode}")

    result = result**pow
    return result
