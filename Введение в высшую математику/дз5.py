# Задание 1
# Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).
import math
from collections import Counter
from random import randint

import matplotlib.pyplot as plt
import numpy as np

#
# def spin_roulette() -> int:
#     return np.random.randint(0, 37)
#
#
# # Задание 2.1
# # Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере рулетки или подбрасывания
# # монетки.
#
# rolls = 10 ** 6
# full_group = (spin_roulette() for _ in range(rolls))
# cnt = Counter(full_group)
# frequences = [value / rolls for key, value in cnt.items()]
# expected_freq = 1 / 37 + 1 / 37
# actual_freq = frequences[0] + frequences[1]
# print(f"Ожидаемая вероятность выпадения или A или B: {expected_freq:.04f}, фактическая вероятность: {actual_freq:.04f}")
#
# # Задание 2.2
# # Сгенерируйте десять выборок случайных чисел х0, …, х9.
# # и постройте гистограмму распределения случайной суммы +х1+ …+ х9.
#
# samples = ((randint(0, 10) for _ in range(10)) for _ in range(10))
# sums = [sum(sample) for sample in samples]
# plt.hist(sums, bins=10)
# plt.show()
# plt.close()

# Задание 3.1
# Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей (через
# биномиальное распределение) и сравните результаты.

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(f"Испытаний: {n}, успехов: {k}, частота: {k / n}")


def bernoulli(k, n):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) / 2 ** n


k = 2
n = 4
print(f"Ожидаемая вероятность получить {k} успехов из {n} испытаний: {bernoulli(k, n)}")

# Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в
# последовательности из n независимых испытаний, взяв другие значения n и k.
k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 3:
        k = k + 1
print(f"Испытаний: {n}, успехов: {k}, частота: {k / n}")


k = 3
n = 5
print(f"Ожидаемая вероятность получить {k} успехов из {n} испытаний: {bernoulli(k, n)}")

