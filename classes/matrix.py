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