import numpy as np


def afunc(array1: np.ndarray, array2: np.ndarray, mode: str = "+", pow: int = 2) -> np.ndarray:
    """Performs addition and subtraction of each element in two arrays
    and raises them by a factor of an integer.

    Args:
        array1: a numerical array
        array2: a numerical array
        mode: addition/subtraction operator '+'/'-' with default param as +
        pow: an integer value which will be used to raise the
        power of the result by the factor, default value is 2

    Returns:
        An array with corresponding addition or subtraction values raised by the factor of pow

    Asserts:
        size mismatch: input arrays should be of same size
        pow should be type int: pow variable should be of type int
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
