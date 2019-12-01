import math


def is_prime(n):
    limit = math.ceil(math.sqrt(n))
    for i in range(2,limit+1):
        if n % i == 0:
            return False
    return True


def problem_seven():
    """
    every prime can be written in the form (6N+1) or (6N-1), so we can use this fact to
    check only numbers in this form.
    """
    count = 2
    index = 0
    while count < 10001:
        index += 6
        if is_prime(index-1):
            count += 1
        if is_prime(index+1):
            count += 1
    if count == 10001:
        return index + 1
    return index - 1
