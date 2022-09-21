"""
B
    Typical usage example:
    num = afunc(1,2,"+")
"""


def afunc(array1, array2, mode="+", pow_para=2) -> int:
    """asic addition and subtraction for each array item
    according to the mode parameter,and powering the array
    with the pow parameter

    Args:
    array1: first array to caLculate the result
    array2: second array to caLculate the result
    mode: default is +, used to indecate how to operate two arrays
    pow: default is 2, used to power up the array

    Returns:
    an int array, which is the result

    Raises:
    TypeError: input type doesn't match
    """
    assert array1.shape == array2.shape, "size mismatch"
    assert isinstance(pow, int), "pow should be type int"

    if mode == "+":
        result = array1 + array2
    elif mode == "-":
        result = array1 - array2
    else:
        raise ValueError(f"mode is either '+' or '-' but got {mode}")

    result = result**pow_para
    return result
