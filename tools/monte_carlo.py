import math
import random


def f(x):
    """
    f(x) is the function we want to integrate. simply returns the result of inputting the input
    number into the function.
    """
    return math.e**(-(x**2))


def integrate(lower, upper, samples):
    """
    uses monte carlo integration methods to estimate integrals
    evaluates the integral of the function f(x), on the interval (lower,upper)
    """

    sample_sum = 0
    for i in range(samples):
        x = random.uniform(lower, upper)
        sample_sum += (f(x))
    return (upper - lower) * (sample_sum / samples)


