from greatest_common_divisor import *


def euler_totient(n):
    """
    computes the value of the euler totient function of input n
    function returns the count of numbers upto n that are relatively prime to n, written phi(n)


    >>> euler_totient(1)
    1

    >>> euler_totient(2)
    1

    >>> euler_totient(9)
    6

    >>> euler_totient(457)
    456

    """
    count = 1
    for x in range(2,n):
        if gcd(n,x)==1:
            count+=1
    return count
