def problem_three():
    return max(prime_factorisation(600851475143))


def prime_factorisation(n):
    factor_list = []
    i = 2

    while i <= n:
        if n % i == 0:
            factor_list.append(i)
            n = n/i
        else:
            i += 1
    return factor_list
