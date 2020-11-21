from sys import argv
from functools import reduce
from itertools import count, cycle


# Задание 01
# (выработка в часах*ставка в час) + премия

if len(argv) == 4:
    try:
        hours, rate, bonus = map(float, argv[1:])
        print("Зарплата сотрудника составила: ", (hours * rate) + bonus)
    except ValueError:
        print("Введите часы, ставку и премию числами через пробел")
else:
    print("Введите три значения: часы, ставку и премию числами через пробел")

# Задание 02
source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [source[index] for index in range(1, len(source)) if source[index] > source[index - 1]]
print(result)

# Задание 03
print([number for number in range(20, 241) if number % 20 == 0 or number % 21 == 0])

# Задание 04
source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [element for element in source_list if source_list.count(element) == 1]
print(result_list)

# Задание 05
new_list = [number for number in range(100, 1001, 2)]
print(reduce(lambda el1, el2: el1 * el2, new_list))

# Задание 06
def int_iterator(number):
    for element in count(number):
        if element > 10:
            break
        else:
            print(element)

def list_iterator(lst):
    count = 0
    for el in cycle(lst):
        if count > 10:
            break
        print(el)
        count += 1

int_iterator(3)
list_iterator(["test1", "test2", "test3"])

# Задание 07
def fact(number):
    """Считает факториал от 1 до полученного числа number и возвращает полученные значения"""
    if number > 0:
        mult = 1
        for number in range(1, number + 1):
            mult *= number
            yield mult
    else:
        print("Функция принимает только целые положительные числа")

for el in fact(-1):
    print(el)
