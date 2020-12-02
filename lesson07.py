# # Задание 01
# from random import randint
# from my_functions import get_digit_from_user
#
#
# class Matrix:
#     """Класс, принимающий на вход список списков,
#     умеющий печатать матрицы в привычном виде и
#     складывать матрицы"""
#
#     def __init__(self, data):
#         if isinstance(data, list):
#             self.data = data
#         else:
#             print("Принимает только список списков на вход!")
#
#     def __str__(self):
#         matrix_string = ""
#         for row in self.data:
#             for value in row:
#                 matrix_string += f"{value:>7}"
#             matrix_string += "\n"
#         return matrix_string
#
#     def __add__(self, other):
#         self.rows = len(self.data)
#         self.columns = len(self.data[0])
#         other.rows = len(other.data)
#         other.columns = len(other.data[0])
#         if self.rows == other.rows and self.columns == other.columns:
#             return Matrix([[x + y for x, y in zip(el1, el2)] for el1, el2 in zip(self.data, other.data)])
#         else:
#             return "Можно сложить только матрицы одинаковой размерности!"
#
#
# def generate_matrix(rows=5, cols=5):
#     return [[randint(-100, 100) for __ in range(cols)] for _ in range(rows)]
#
#
# matrix1 = Matrix(generate_matrix(2, 3))
# matrix2 = Matrix(generate_matrix())
# matrix3 = Matrix(generate_matrix())
# matrix4 = Matrix(generate_matrix())
#
# print(matrix1)
# print(matrix2)
# print(matrix3)
# print(matrix4)
#
# print(matrix1 + matrix2)
# print(matrix2 + matrix3)
# print(matrix2 + matrix3 + matrix4)
#

# Задание 02
