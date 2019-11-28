import math


def factors(n):
    """
    function returns all the numbers that divide the input number, n
    >>> factors(24)
    [1, 2, 3, 4, 6, 8, 12, 24]

    >>> factors(15)
    [1, 3, 5, 15]

    >>> factors(17)
    [1, 17]
    """
    factor_list = []
    limit = math.ceil(n/2)
    for x in range(1,limit+1):
        if n % x == 0:
            factor_list.append(x)
    if n != 1:
        factor_list.append(n)
    return factor_list

