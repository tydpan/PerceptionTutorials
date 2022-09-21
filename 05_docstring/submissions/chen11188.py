import numpy as np


def afunc(array1: np.ndarray, array2: np.ndarray, mode: str = "+", pow: int = 2) -> np.ndarray:
    """performs addition or subtraction of two arrays
    and power them by an integer.

    Args:
        array1: numerical array
        array2: numerical array
        mode: addition/subtraction operator
        pow: the power of the result
    Returns:
        an array by operating addition or subtraction
         and power them by an integer
    Raises:
        size mismatch: two arrays need to be the same size
        pow should be type int: the variable need to be integer
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
