import random
from typing import Union


def find_smallest(lst: Union[list, set, tuple]) -> int:
    """
    :param lst: список чисел
    :return: индекс минимального элемента
    """

    smallest = lst[0]
    index_smallest = 0

    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            index_smallest = i
    return index_smallest


def selection_sort(arr: Union[list, set, tuple]) -> list:
    """
    Сортировка выбором
    :param arr: список чисел
    :return: отсортированный список чисел
    """

    new_arr = list()
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([random.randint(0, 100) for _ in range(100)]))
