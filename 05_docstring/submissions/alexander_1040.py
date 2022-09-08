"""
This module defines the function afunc, which does simple addition and
subtraction using two arrrays, raises that result to a specified power,
and returns the resulting array.
"""
from array import array


def afunc(array_1: array, array_2: array, mode="+", power=2):
    """
    Args:
        array_1 (array): First list of integers to be used
        array_2 (array): Second list of integers to be used
        mode (str, optional): has two different modes, add(+) and subtract(-).
                              Defaults to "+".
        power (int, optional): raises result to specified power. Defaults to 2.

    Raises:
        ValueError: the mode variable was given an incorrect string value

    Returns:
        result (array): The resulting array, using given two arrays, either
        added or subtracted based on mode, then raised to the power specified
        by power.
    """
    assert array_1.shape == array_2.shape, "size mismatch"
    assert isinstance(power, int), "power should be type int"

    if mode == "+":
        result = array_1 + array_2
    elif mode == "-":
        result = array_1 - array_2
    else:
        raise ValueError(f"mode is either '+' or '-' but got {mode}")

    result = result**power
    return result
