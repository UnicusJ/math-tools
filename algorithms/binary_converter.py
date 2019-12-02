def binary_convert(num):
    """
    converts a base 10 integer into it's binary form

    >>> binary_convert(16)
    '10000'

    >>> binary_convert(1)
    '1'

    >>> binary_convert(45)
    '101101'

    """
    output = ''
    while num != 0 and num != 1:
        output = str(num%2) + output
        num = num // 2
    output = str(num) + output
    return output
