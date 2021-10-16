from numpy import ndarray


def truncate_number_string(n):
    n_list = n.split(".")
    integer = n_list[0]
    decimal = n_list[1][1:3]
    exponent = n.split("e")[1]
    if exponent == 0:
        return f"{integer}.{decimal}e00"
    elif exponent == 1:
        return f"{integer}.{decimal}e01"
    else:
        return f"{integer}.{decimal}e{exponent}"


def array_to_string(array: ndarray):
    array_string = [truncate_number_string(str(element)) for element in list(array)]
    return f"[{array_string[0]}", f" {array_string[1]}]"
