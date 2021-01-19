# Задание 01
from random import randint


class Matrix:
    """Класс, принимающий на вход список списков,
    умеющий печатать матрицы в привычном виде и
    складывать матрицы"""

    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            print("Принимает только список списков на вход!")

    def __str__(self):
        """Переводит матрицу в строку для удобства вывода"""
        matrix_string = ""
        for row in self.data:
            for value in row:
                matrix_string += f"{value:>7}"
            matrix_string += "\n"
        return matrix_string

    def __add__(self, other):
        """Складывает две матрицы одинакового размера"""
        self.rows = len(self.data)
        self.columns = len(self.data[0])
        other.rows = len(other.data)
        other.columns = len(other.data[0])
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([[x + y for x, y in zip(el1, el2)] for el1, el2 in zip(self.data, other.data)])
        else:
            return "Можно сложить только матрицы одинаковой размерности!"


def generate_matrix(rows=5, cols=5):
    return [[randint(-100, 100) for __ in range(cols)] for _ in range(rows)]


matrix1 = Matrix(generate_matrix(2, 3))
matrix2 = Matrix(generate_matrix())
matrix3 = Matrix(generate_matrix())
matrix4 = Matrix(generate_matrix())

print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)

print(matrix1 + matrix2)
print(matrix2 + matrix3)
print(matrix2 + matrix3 + matrix4)

# Задание 02
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name
        self._cloth_consumption = 0

    @property
    def cloth_consumption(self):
        return self._cloth_consumption

    @abstractmethod
    def calculate_cloth(self, size):
        pass


class Coat(Clothes):
    def calculate_cloth(self, size):
        self._cloth_consumption = round(size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def calculate_cloth(self, size):
        self._cloth_consumption = round(size * 2 + 0.3, 2)


coat = Coat("Пальто")
coat.calculate_cloth(42)
print(f"Ушло ткани на пальто: {coat.cloth_consumption} ед.")

suit = Suit("Костюм с отливом")
suit.calculate_cloth(1.86)
print(f"Ушло ткани на костюм: {suit.cloth_consumption} ед.")

print(f"Ушло ткани всего: {coat.cloth_consumption + suit.cloth_consumption} ед.")


# Задание 03
class Cell:
    def __init__(self, units):
        self.units = units

    def __str__(self):
        return str(self.units)

    def __add__(self, other):
        return Cell(self.units + other.units)

    def __sub__(self, other):
        if self.units - other.units > 0:
            return Cell(self.units - other.units)
        else:
            return "Результат операции <= 0"

    def __mul__(self, other):
        return Cell(self.units * other.units)

    def __floordiv__(self, other):
        return Cell(self.units // other.units)

    def make_order(self, arg):
        unit = "@"
        new_string = ""
        for _ in range(self.units // arg):
            new_string += unit * arg + "\n"
        new_string += unit * (self.units % arg)

        return new_string


cell1 = Cell(15)
cell2 = Cell(10)
cell3 = Cell(5)

print(cell1.make_order(4))

print(cell1 + cell2)
print(cell1 + cell2 + cell3)

print(cell1 - cell2)
print(cell1 - cell2 - cell3)

print(cell1 * cell2)
print(cell1 * cell2 * cell3)

print(cell1 // cell2)
