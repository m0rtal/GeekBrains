from typing import Union


def factorial(num: int) -> int:
    """
    Вычисляет факториал числа
    :param num: целое положительное число
    :return: факториал предоставленного числа
    """
    assert isinstance(num, int), "Только положительные целые числа!"
    if num == 1:
        return 1
    elif num > 1:
        return num * factorial(num - 1)
    else:
        print("Только положительные целые числа!")
        return -1


print(factorial(5))


def summ(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + summ(arr)


print(summ(list(range(101))))
