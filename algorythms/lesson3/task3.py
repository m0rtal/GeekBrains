"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint


run = True

while run:
    items_cnt = int(input("Введите количество элементов в списке: "))

    array = [randint(-100, 100) for _ in range(items_cnt)]
    print(array)

    min_index = array.index(min(array))
    max_index = array.index(max(array))

    array[min_index], array[max_index] = array[max_index], array[min_index]
    print(array)

    run = input("Продолжить [y/n]: ") == 'y' or False
