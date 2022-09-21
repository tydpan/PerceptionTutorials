import numpy as np


def afunc(
    array1: Union[int, float], array2: Union[int, float], mode: str = "+", pow: int = 2
) -> Union[int, float]:
    """Simple Math Caculation
    Caculates addition, subtraction between array1 and array2 arguments,
    and return the power of pow of the result.

    Args:
        array1:
            The given formal argument used as augend or minuend
        array2:
            The given formal argument used as addend or minuend
        mode:
            variable to demonstrate either addition or substraction
        pow:
            define the number of powers used in the returning value

    Returns:
        an int or float after doing all the caculation

    Raises:
        Error: Incompatible types in assignment
    """

    assert array1.shape == array2.shape, "size mismatch"
    assert type(pow) == int, "pow should be type int"

    if mode == "+":
        result = array1 + array2
    elif mode == "-":
        result = array1 - array2
    else:
        raise ValueError(f"mode is either '+' or '-' but got {mode}")

    result = result ** pow
    return result
