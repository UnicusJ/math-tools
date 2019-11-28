def gcd(a,b):
    """
    returns the greatest number that divides both a and b
    >>> gcd(10,5)
    5
    >>> gcd(10,3)
    1
    >>> gcd(10,0)
    10
    >>> gcd(5,10)
    5
    """
    if b > a:
    #swap inputs if b > a
        a, b = b, a
    if b == 0:
    #base case, when b is reduced to 0, the gcd is a
        return a
    else:
    #gcd(a,b) = gcd(b,a%b), so we can reduce problem size (Euclidean Algorithm)
        return gcd(b, a % b)

