def collatz(n):
    """
    returns a list containing the full collatz path of input number n.
    the rule is as follows:
    if n is even, replace n with n/2
    else, replace n with 3n + 1

    >>> collatz(24)
    [24, 12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

    >>> collatz(4)
    [4, 2, 1]

    >>> collatz(25)
    [25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    current = n
    sequence = [n]

    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3*current + 1
        sequence.append(current)
    return sequence

