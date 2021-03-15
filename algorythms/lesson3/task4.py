"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint
from collections import Counter

while input("Поехали? [y/n]: ").lower() == 'y':
    items_cnt = int(input("Введите количество элементов в списке: "))
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]
    print(array)
    print(
        f"Самое часто встречаемое число в списке: {Counter(array).most_common(1)[0][0]} повторяется {Counter(array).most_common(1)[0][1]} раз")
