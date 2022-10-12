import numpy as np


def afunc(array1, array2, mode="+", pow=2):
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="This is tutorial for argparse.")
    # add your code here
    parser.add_argument(
        "mode",
        metavar="M",
        help="""
        mode defines which summation operation to perform on matrices
        and is limited to '+' or '-'
        """,
        default="+",
        type=str,
    )

    parser.add_argument(
        "pow",
        metavar="P",
        help="pow raises each element in the matrix to specified power",
        default=2,
        type=int,
    )

    parser.add_argument("print_hello", action="store_true")
    # add your code here
    args = parser.parse_args()
    print(args)

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = afunc(a, b, args.mode, args.pow)
    print(result)
    if args.print_hello:
        print("Hello!")
