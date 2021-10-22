from numpy import ndarray
from typing import Union


def is_int(n: str) -> bool:
    """
    Returns True if a given string is an integer. Else
    returns False
    """
    try:
        n_int = int(n)
        if n == n_int:
            return True
    except ValueError:
        return False


def fix_decimal_number(decimal: int, digits: int) -> int:
    """
    Given the decimal part of a number this function fixes
    the decimal number's digits by truncating it or adding
    ceros.

    Example:
    n = 1.234
    fix_decimal_number(234, 2)
    >>> 23
    fix_decimal_number(234, 4)
    >>> 2340
    """
    decimal = str(decimal)
    if len(decimal) == digits:
        return int(decimal)

    elif len(decimal) < digits:
        for _ in range(digits - len(decimal)):
            decimal += "0"
        return int(decimal)

    else:
        return int(decimal[1:3])


def decompose_number(n: float) -> tuple[int, int, int]:
    """
    Decomposes a given number and returns its integer,
    decimal and exponent part.

    Example:
    decompose_number(1.234e-4)
    >>> (1, 234, -4)
    """
    n_str = str(n)
    if "." not in n_str:
        return n, 0, 0

    integer, after_comma = n_str.split(".")
    if "e" not in n_str:
        return int(integer), int(after_comma), 0

    else:
        decimal, exponent = after_comma.split("e")
        return int(integer), int(decimal), int(exponent)


def format_number(n: Union[float, int]) -> str:
    """
    This function formats a given number by adding an exponent
    and decimal part or fixing their total digits if needed.
    """
    if is_int(n):
        return f"{n}e00"

    integer, decimal, exponent = decompose_number(n)
    fixed_decimal = fix_decimal_number(decimal, 2)

    if exponent == 0:
        return f"{integer}.{fixed_decimal}e00"
    elif exponent == 1:
        return f"{integer}.{fixed_decimal}e01"
    else:
        return f"{integer}.{fixed_decimal}e{exponent}"


def array_to_string(array: ndarray) -> tuple[str, str]:
    truncated_array = [format_number(element) for element in list(array)]
    return f"[{truncated_array[0]}", f" {truncated_array[1]}]"
