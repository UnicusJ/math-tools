# this problem is essentially trying to calculate LCM(1,2,3,4, ... ,20)
# we know that LCM(a,b) = ab / GCD(a,b), and we can extend this by observing LCM(a,b,c) = LCM(a,LCM(b,c)
# thus we can use a recursive approach to find our solution


def problem_five(factor_list):
    a = factor_list[0]
    b = factor_list[1]
    if len(factor_list) == 2:
        return (a*b)//gcd(a, b)
    else:
        return (a * problem_five(factor_list[1:])) // gcd(a,problem_five(factor_list[1:]))


def gcd(a,b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)