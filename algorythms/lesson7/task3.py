"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
не меньше медианы, в другой — не больше медианы."""

import random

m = int(input("Введите m для определения длины массива по формуле (2m+1): "))
array_len = 2 * m + 1

random_array = [random.randint(-10, 10) for _ in range(array_len)]
print(random_array)


def find_mean(array):
    while len(array) > 1:
        array.remove(max(array))
        array.remove(min(array))
    return array[0]


print(f"Медиана списка {sorted(random_array)} = {find_mean(random_array)}")
