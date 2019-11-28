def prime_factorisation(n):
    """
    computes the prime factorisation of a number n

    >>> prime_factorisation(10)
    'Prime factors of 10 are: [2, 5]'

    >>> prime_factorisation(8762)
    'Prime factors of 8762 are: [2, 13, 337]'

    >>> prime_factorisation(0)
    'Prime factors of 0 are: []'

    """
    original_num = n
    factor_list = []
    i = 2

    while i <= n:
        if n % i == 0:
            factor_list.append(i)
            n = n/i
        else:
            i += 1
    return 'Prime factors of ' + str(int(original_num)) + ' are: ' + str(factor_list)

