# import numpy as np


def afunc(array1, array2, mode="+", pow=2):
    """Perform the addition and substraction of array1 and array2,
    then take the power of the result, then return out it.
    Args:
        array1: the first array of integers.
        array2: the second array of integers.
        mode: the mode of operation style, either addition "+" or subtraction "-".  # noqa: E501
              Default parameter is "+"
        pow: the integer power will be applied onto the result.
    Returns:
        the power applied onto the addition or substraction
        in between array1 and array2.
    Raises:
        SizeError: unmatched size error of these two array arguments.
        TypeError: the pow argument is not an int.
        ValueError: the mode argument is not "+" or "-".
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
