import math


def is_prime(n):
    """returns True if n is composite, and False otherwise (if n is prime)"""
    if n <= 1:
        return False

    lim = int(math.sqrt(n))+1
    for x in range(2,lim):
        if n % x == 0:
            return False
    return True


def twin_primes(n):
    """
    prints all sets of twin primes below input n
    twin primes are pairs of primes in the form (6n-1),(6n+1) where both are primes
    the algorithm prints such pairs, by going through the multiples of 6, and checking the number above and below

    >>> twin_primes(10)
    (3,5) (5,7) .

    >>> twin_primes(100)
    (3,5) (5,7) (11,13) (17,19) (29,31) (41,43) (59,61) (71,73) .

    >>> twin_primes(3)
    No twin primes below 3

    """
    if n <= 4:
        print('No twin primes below {}'.format(n))
    else:
        print('(3,5) ', end='')
        count = 6
        while count < n:
            if is_prime(count-1) and is_prime(count+1):
                print('({},{}) '.format(count-1,count+1), end='')
            count += 6
        print('.')


twin_primes(100)
