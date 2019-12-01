from greatest_common_divisor import *
import math


def lcm(num_list):
    """
    computes the lowest common multiple of a list of input numbers
    function uses recursion and uses the fact that
    - LCM(a,b) = ab / GCD(a,b)
    and
    - LCM(a,b,c) = LCM(a, LCM(b, c))

    >>> lcm([3,4,5])
    60

    >>> lcm([1,2,3,4,5,6,7,8,9,10])
    2520

    >>> lcm([1])
    'Please enter a list containing more than 1 number.'

    >>> lcm([0,1])
    'The LCM of zero does not exist, please remove it from input list.'

    >>> lcm([1,-2])
    2

    """
    if len(num_list) == 1:
        return 'Please enter a list containing more than 1 number.'
    if 0 in num_list:
        return 'The LCM of zero does not exist, please remove it from input list.'

    a = abs(num_list[0])
    b = abs(num_list[1])
    if len(num_list) == 2:
        return (a*b)//gcd(a, b)
    else:
        return (a * lcm(num_list[1:])) // gcd(a, lcm(num_list[1:]))
