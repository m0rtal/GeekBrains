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
#         """Переводит матрицу в строку для удобства вывода"""
#         matrix_string = ""
#         for row in self.data:
#             for value in row:
#                 matrix_string += f"{value:>7}"
#             matrix_string += "\n"
#         return matrix_string
#
#     def __add__(self, other):
#         """Складывает две матрицы одинакового размера"""
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
#
# # Задание 02
# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     def __init__(self, size, name):
#         self.name = name
#
#     @abstractmethod
#     def cloth_consumption(self):
#         pass
#
#     def _total_cloth(self, cloth1, cloth2):
#         return cloth1.cloth_consumption + cloth2.cloth_consumption
#
#
# class Coat(Clothes):
#     def __init__(self, size, name="Пальто"):
#         super().__init__(size, name)
#         self._cloth_consumption = round(size / 6.5 + 0.5, 2)
#
#     @property
#     def cloth_consumption(self):
#         return self._cloth_consumption
#
#
# class Suit(Clothes):
#     def __init__(self, size, name="Костюм с отливом"):
#         super().__init__(size, name)
#         self._cloth_consumption = round(size * 2 + 0.3, 2)
#
#     @property
#     def cloth_consumption(self):
#         return self._cloth_consumption
#
#
# coat = Coat(42)
# print(f"Ушло ткани на пальто: {coat.cloth_consumption} ед.")
#
# suit = Suit(1.86)
# print(f"Ушло ткани на костюм: {suit.cloth_consumption} ед.")
#
# print(f"Ушло ткани всего: {Clothes._total_cloth(Clothes, coat, suit)} ед.")

# Задание 03
