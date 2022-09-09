"""learning doc"""


def afunc(array1, array2, mode="+"):
    """use two arrays for the shape"""
    assert array1.shape == array2.shape, "size mismatch"
    assert isinstance(pow) == int, "pow should be type int"

    if mode == "+":
        result = array1 + array2
    elif mode == "-":
        result = array1 - array2
    else:
        raise ValueError(f"mode is either '+' or '-' but got {mode}")

    result = result**pow
    return result
