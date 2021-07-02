""" 1. Задание (в программе)
Нарисуйте график функции: y(x) = k∙cos(x – a) + b для некоторых (2-3 различных)
значений параметров k, a, b
"""
from math import cos, sin

import matplotlib.pyplot as plt
import numpy as np
from random import randint

x = np.linspace(-np.pi, np.pi, 101)
for i in range(3):
    k = randint(1, 5)
    a = randint(1, 5)
    b = randint(1, 5)
    y = k * np.cos(x - a) + b
    plt.plot(x, y, label=f"y{i}")

plt.legend()
plt.grid(True)
plt.show()
plt.close()

""" Напишите код, который будет переводить полярные координаты в декартовы. """


def convert_polar_to_decart(r, a):
    return round(r * cos(a), 2), round(r * sin(a), 2)


""" Напишите код, который будет рисовать график окружности в полярных координатах. """
r = 3
a = np.linspace(0, 2 * np.pi, 100)
x = r * np.cos(a)
y = r * np.sin(a)

plt.figure(figsize=(r * 2, r * 2))
plt.polar(x, y)
plt.show()
plt.close()

""" Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах"""

x = np.linspace(0, 5, 101)
y = 2 * x + 1
plt.polar(x, y)
plt.show()
plt.close()

""" Решите систему уравнений 
exp(x) + x*(1 – y) = 1
y = x^2 – 1
"""
from scipy.optimize import fsolve


def equations(p):
    x, y = p
    return np.exp(x) + x * (1 - y) - 1, x ** 2 - y - 1


x1, y1 = fsolve(equations, (1, 1))
print(x1, y1)

""" Решите систему уравнений 
exp(x) + x*(1 – y) - 1 > 0
y = x^2 – 1
"""


def equations(p):
    x, y = p
    if np.exp(x) + x * (1 - y) - 1 > 0:
        return np.exp(x) + x * (1 - y) - 1, x ** 2 - y - 1
    else:
        return None, x ** 2 - y - 1


x1, y1 = fsolve(equations, (1, 1))
print(x1, y1)
