import math
import random

class Complex:

    def __init__(self, r, i):
        self.real = r
        self.im = i

    def __str__(self):
        """prints the complex number in form a + bi"""
        if self.im != 1 and self.im != -1:
            if self.im < 0:
                s = str(self.real) + ' - ' + str(abs(self.im)) + 'i'
            else:
                s = str(self.real) + ' + ' + str(self.im)+'i'
        elif self.im == 1:
            s = str(self.real) + ' + i'
        else:
            s = str(self.real) + ' - i'
        return s

    def __repr__(self):
        return 'Complex({},{})'.format(self.real, self.im)

    def __add__(self, com):
        """adds two complex numbers in form a + bi"""
        real_part = self.real + com.real
        imaginary_part = self.im + com.im
        return Complex(real_part, imaginary_part)

    def __sub__(self, com):
        """subtracts two complex numbers in form a + bi"""
        real_part = self.real - com.real
        imaginary_part = self.im - com.im
        return Complex(real_part, imaginary_part)

    def __mul__(self, com):
        """multiplies two complex numbers in form a + bi"""
        if type(com) == int :
            real_part = self.real * com
            imaginary_part = self.im * com
            return Complex(real_part, imaginary_part)

        real_part = (self.real * com.real) - (self.im * com.im)
        imaginary_part = (self.real * com.im) + (self.im * com.real)
        return Complex(real_part, imaginary_part)

    def __pow__(self, power):
        new_com = Complex(self.real, self.im)
        for x in range(power-1):
            new_com = new_com * self

        return new_com

    def conjugate(self):
        """returns the complex conjugate in form a + bi"""
        return Complex(self.real, -self.im)

    def polar(self):
        """converts complex number into polar form (r cis theta)"""
        r = math.sqrt(self.real**2 + self.im**2)
        arg = math.atan(self.im / self.real)
        return str(round(r, 3)) + ' cis ' + str(round(arg, 3))

    def mod(self):
        """returns the modulus of the complex number"""
        return math.sqrt(self.real**2 + self.im**2)

    def complex_to_matrix(self):
        return Matrix(2, 2, [[self.real, -self.im], [self.im, self.real]])
