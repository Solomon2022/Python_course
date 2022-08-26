# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string_el = ''
        for el in self.matrix:
            for el_el in el:
                string_el += str(el_el) + '   '
            string_el += '\n'
        return string_el

    def equal_matrix(matrix_1, matrix_2):
        if len(matrix_1) == len(matrix_2):
            for el_1, el_2 in zip(matrix_1, matrix_2):
                if len(el_1) != len(el_2):
                    return False
            return True
        else:
            return False

    def __add__(self, other):
        if Matrix.equal_matrix(self.matrix, other.matrix):
            my_list = []
            result_list = []
            for el_1, el_2 in zip(self.matrix, other.matrix):
                for el_el_1, el_el_2 in zip(el_1, el_2):
                    my_list.append(el_el_1 + el_el_2)
                result_list.append(my_list)
                my_list = []
            return Matrix(result_list)
        else:
            return 'Программа не способна сложить такие матрицы'


matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[5, 6], [7, 8]])
matrix_3 = Matrix([[9, 10], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1 + matrix_2 + matrix_3)
