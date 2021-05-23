"""Напишите код на Python, реализующий расчет длины вектора, заданного его координатами"""
import math


class Vector:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f"x={self.x}, y={self.y}, z={self.z}"

    @property
    def length(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)


v1 = Vector(10, 10, 10)
v2 = Vector(0, 0, -10)

v3 = v1 + v2

print(f"Длина вектора {v3}: {v3.length}")
