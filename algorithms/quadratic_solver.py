import math


def solve_quadratic(a, b, c):
    """
    solves quadratic equation in form ax^2+bx+c

    >>> solve_quadratic(1,-4,4)
    The solution has one repeated root: 2.0

    >>> solve_quadratic(1,1,1)
    The solution has unique roots: (-0.5+0.8660254037844386j) and (-0.5-0.8660254037844386j)

    >>> solve_quadratic(0,1,1)
    Not a quadratic!

    """

    if a == 0:
        print('Not a quadratic!')
    else:
        discriminant = b**2-(4*a*c)

        root_one = 0
        root_two = 0

        if discriminant >= 0:
            root_one = (-b+math.sqrt(discriminant))/(2*a)
            root_two = (-b-math.sqrt(discriminant))/(2*a)
        elif discriminant < 0:
            root_one = complex(-b/(2*a),math.sqrt(-discriminant)/(2*a))
            root_two = complex(-b/(2*a),-math.sqrt(-discriminant)/(2*a))

        if root_one == root_two:
            print('The solution has one repeated root: ' + str(root_one))
        else:
            print('The solution has unique roots: ' + str(root_one) + ' and ' + str(root_two))
