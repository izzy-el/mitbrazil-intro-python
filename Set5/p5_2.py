class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def size(self):
        return (len(self.lst), len(self.lst[0]))

    def get(self, r, c):
        return self.lst[r][c]

    def set(self, r, c, val):
        self.lst[r][c] = val
        return None

    def row(self, n):
        _list = []

        for nums in self.lst[n]:
            _list.append(nums)

        return _list

    def col(self, n):
        _list = []

        for index in range(0, self.size()[0]):
            _list.append(self.lst[index][n])

        return _list

    def transpose(self):
        matrix = []
        temp_list = []

        for row in range(self.size()[1]):
            for col in range(self.size()[0]):
                temp_list.append(self.get(col, row))
            matrix.append(temp_list)
            temp_list = []

        return Matrix(matrix)

    # Dunder Methods
    def __add__(self, other):
        matrix = []
        temp_list = []

        if isinstance(other, Matrix) and self.size() == other.size():
            for row_one, row_two in zip(self.lst, other.lst):
                for col_one, col_two in zip(row_one, row_two):
                    temp_list.append(col_one + col_two)
                matrix.append(temp_list)
                temp_list = []
            return Matrix(matrix)

        elif isinstance(other, Matrix) and self.size() != other.size():
            return None

        elif isinstance(other, (int, float)):
            for row in self.lst:
                for col in row:
                    temp_list.append(col + other)
                matrix.append(temp_list)
                temp_list = []

            return Matrix(matrix)

        else:
            return None

    def __sub__(self, other):
        matrix = []
        temp_list = []

        if isinstance(other, Matrix) and self.size() == other.size():
            for row_one, row_two in zip(self.lst, other.lst):
                for col_one, col_two in zip(row_one, row_two):
                    temp_list.append(col_one - col_two)
                matrix.append(temp_list)
                temp_list = []
            return Matrix(matrix)

        elif isinstance(other, Matrix) and self.size() != other.size():
            return None

        elif isinstance(other, (int, float)):
            for row in self.lst:
                for col in row:
                    temp_list.append(col - other)
                matrix.append(temp_list)
                temp_list = []

            return Matrix(matrix)

        else:
            return None

    def __mul__(self, other):
        matrix = []
        temp_list = []
        value = 0

        if isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            for row_first in range(len(self.lst)):  
                for row_second in range(len(other.lst[0])):  
                    for column_second in range(len(other.lst)):  
                        value += self.lst[row_first][column_second] * other.lst[column_second][row_second]  
                    temp_list.append(value)      
                    value = 0   
                matrix.append(temp_list) 
                temp_list = []
            
            return Matrix(matrix)

        elif isinstance(other, Matrix) and self.size()[1] != other.size()[0]:
            return None

        elif isinstance(other, (int, float)):
            for row in self.lst:
                for col in row:
                    temp_list.append(col * other)
                matrix.append(temp_list)
                temp_list = []

            return Matrix(matrix)

        else:
            return None
