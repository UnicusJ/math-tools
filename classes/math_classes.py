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


class Matrix:
    def __init__(self, m, n, value_list=None):
        self.row_num = m
        self.col_num = n
        self.rows = [[0]*n for x in range(m)]

        if value_list is not None:
            self.set_values(value_list)

    def __str__(self):

        longest_num = len(str(self.rows[0][0]))
        for list in self.rows:
            for val in list:
                if len(str(val)) > longest_num:
                    longest_num = len(str(val))

        string = ''
        for list in self.rows:
            row = ""
            for val in list:
                row += str(val) + " "*(longest_num+1 - len(str(val)))
            string += row + '\n'
        return string

    def __repr__(self):
        return 'Matrix({},{})'.format(self.row_num, self.col_num)

    def __add__(self, mat):
        """performs pairwise addition of two matrices of equal rank"""
        if self.get_rank() == mat.get_rank():
            new_mat = Matrix(self.row_num, self.col_num)

            for m in range(0, self.row_num):
                for n in range(0, self.col_num):
                    new_mat.rows[m][n] = self.rows[m][n] + mat.rows[m][n]
            return new_mat
        else:
            return 'Matrices not of same rank'

    def __sub__(self, mat):
        """performs pairwise subtraction of two matrices of equal rank"""
        if self.get_rank() == mat.get_rank():
            new_mat = Matrix(self.row_num, self.col_num)

            for m in range(0, self.row_num):
                for n in range(0, self.col_num):
                    new_mat.rows[m][n] = self.rows[m][n] - mat.rows[m][n]
            return new_mat
        else:
            return 'Matrices not of same rank'

    def __mul__(self, mat):
        """performs proper matrix multiplication. note: matrices must agree on inner dimensions. also performs pairwise
        scalar multiplication"""
        new_mat = Matrix(self.row_num, self.col_num)
        if type(mat) == int:
            for m in range(0, self.row_num):
                for n in range(0, self.col_num):
                    new_mat.rows[m][n] = self.rows[m][n] * 2
            return new_mat

        if self.col_num != mat.row_num:
            return "not defined"

        '''rows of self'''
        for m in range(0, self.row_num):
            '''cols of mat'''
            for m2 in range(0, mat.col_num):
                '''rows of mat'''
                for n in range(0, mat.row_num):
                    new_mat.rows[m][m2] += self.rows[m][n] * mat.rows[n][m2]

        return new_mat

    def __pow__(self, mat):
        """performs pairwise matrix multiplication"""
        if self.get_rank() == mat.get_rank():
            new_mat = Matrix(self.row_num, self.col_num)

            for m in range(0, self.row_num):
                for n in range(0, self.col_num):
                    new_mat.rows[m][n] = self.rows[m][n] * mat.rows[m][n]
            return new_mat
        else:
            return 'Matrices not of same rank'

    def get_rank(self):
        """returns the rank (dimensions) of a matrix"""
        return '{}x{}'.format(self.row_num, self.col_num)

    def set_value(self, m, n, val):
        """changes the value of position (m,n) in the matrix. note: user index starts at 1 for ease of use"""
        self.rows[m-1][n-1] = val

    def set_values(self,value_list):
        """takes a list of lists as an argument, with each list in the list being a row in the matrix. the existing
        matrix is then mutated to contain the specified values"""
        matrix_values = value_list

        for x in range(len(matrix_values)):
            for y in range(len(matrix_values[1])):
                self.set_value(x+1, y+1, matrix_values[x][y])

    def set_all(self, val):
        for m in range(0, self.row_num):
            for n in range(0, self.col_num):
                self.rows[m][n] = val

    def transpose(self):
        transpose = Matrix(self.col_num, self.row_num)
        for m in range(0, self.row_num):
            for n in range(self.col_num):
                transpose.rows[n][m] = self.rows[m][n]
        return transpose

    def set_random(self, maximum=9):
        for m in range(0, self.row_num):
            for n in range(0, self.col_num):
                self.rows[m][n] = random.randint(1, maximum)

    def cross(self, mat):

        if self.get_rank() != '3x1' or mat.get_rank() != '3x1':
            return 'can only calculate cross product of 3x1 vectors'

        s1 = (self.rows[1][0] * mat.rows[2][0]) - (self.rows[2][0] * mat.rows[1][0])
        s2 = (self.rows[2][0] * mat.rows[0][0]) - (self.rows[0][0] * mat.rows[2][0])
        s3 = (self.rows[0][0] * mat.rows[1][0]) - (self.rows[1][0] * mat.rows[0][0])

        new_mat = Matrix(3, 1)
        new_mat.set_value(0, 0, s1)
        new_mat.set_value(1, 0, s2)
        new_mat.set_value(2, 0, s3)

        return new_mat

    def matrix_to_complex(self):
        if self.get_rank() != '2x2':
            return 'Matrix must be 2x2'
        else:
            return Complex(self.rows[0][0], self.rows[1][0])


class Graph:
    def __init__(self,dict):
        self.data = dict

    def get_node_number(self):
        return len(self.data)

    def get_edge_number(self):
        pass

    def get_edge_list(self):
        edge_list = []
        for key in self.data:
            for value in self.data[key]:
                print(sorted([key,value]))
                if sorted([key, value]) not in edge_list:
                    edge_list.append((key, value))
        return edge_list

    def get_neighbours(self, node):
        return self.data[node]

    def get_degree(self, node):
        return len(self.data[node])

    def add_node(self, node):
        self.data[node] = []

    def add_edge(self, n1, n2):
        self.data[n1] += n2
        self.data[n2] += n1




g= { "a" : ["c"],  "b" : ["c", "e"], "c" : ["a", "b", "d", "e"],  "d" : ["c"],  "e" : ["c", "b"],  "f" : []  }

graph = Graph(g)
l = graph.get_edge_list()
print(l)
print(graph.get_neighbours('c'))
print(graph.get_degree('c'))


graph.add_edge('a','b')
l = graph.get_edge_list()
print(l)

print(sorted(('c','b')))