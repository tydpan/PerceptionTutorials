

def afunc(array1, array2, mode="+", pow=2):
    """Produces the sum or difference of two arrays then raise to nth powers.

    Takes the sum or difference of two same-shaped arrays array1 and array 2,
    then raise the sum (difference) to n (integer) powers.

    Args:
        array1: the first array.
        array2: the second array.
        mode: the mode of operating the two arrays, either "+" or "-".
            Default "+".
        pow: the integer power to raise the sum (difference) to. Default to 2.

    Returns:
        An array as the result of summing (subtracting) two arrays and raising
        the sum (difference) to nth powers.

    Raises:
        SizeError: A "size mismatch" error if the shapes of two arrays do not
             match.
        TypeError: An error if the pow argument is not an integer type.
        ValueError: An error if the mode argument is not "+" or "-".
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
