""" Задание 1.2
Напишите код на Python, реализующий расчет длины вектора, заданного его координатами"""
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

""" Задание 2
почему прямые не кажутся перпендикулярными?
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 21)
y = 3 * x + 1
y2 = (-1 / 3) * x + 1
plt.plot(x, y)
plt.plot(x, y2)
plt.show()
plt.close()

""" Ответ:
Потому что не совпадает масштаб осей
"""

""" Задание 3
Напишите код на Python, реализующий построение графиков:
1. окружности,
2. эллипса,
3. гиперболы. 
"""

# Окружность
x = np.linspace(-5, 5, 1001)
r = 3
y1 = np.sqrt((r ** 2 - x ** 2))
y2 = -np.sqrt((r ** 2 - x ** 2))

plt.figure(figsize=(r * 2, r * 2))
plt.plot(x, y1, c="r")
plt.plot(x, y2, c="r")
plt.show()
plt.close()

# Эллипс
x = np.linspace(-5, 5, 1001)
a = 3
b = 1
y1 = np.sqrt(b ** 2 * (1 - x ** 2 / a ** 2))
y2 = -np.sqrt(b ** 2 * (1 - x ** 2 / a ** 2))

plt.figure(figsize=(a * 2, b * 2))
plt.plot(x, y1, c="r")
plt.plot(x, y2, c="r")
plt.show()
plt.close()

# Гипербола
x = np.linspace(-5, 5, 1001)
a = 3
b = 1
y1 = np.sqrt(b ** 2 * (1 + x ** 2 / a ** 2))
y2 = -np.sqrt(b ** 2 * (1 + x ** 2 / a ** 2))

plt.figure(figsize=(a * 2, b * 2))
plt.plot(x, y1, c="r")
plt.plot(x, y2, c="r")
plt.show()
plt.close()

""" Задание 5 """

# 1) Нарисуйте трехмерный график двух параллельных плоскостей.
from pylab import figure, show, close
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z1 = 2 * X + 3 * Y
Z2 = 2 * X + 3 * Y + 50
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
show()
close()

# 2) Нарисуйте трехмерный график двух любых поверхностей второго порядка.
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z1 = X**3 + Y**3
ax.plot_surface(X, Y, Z1)
show()
close()

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z2 = -np.sqrt(X**3 * Y**3)-200
ax.plot_surface(X, Y, Z2)
show()
close()
