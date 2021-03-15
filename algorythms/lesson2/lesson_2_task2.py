"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
и 2 нечетные (3 и 5).
"""

even_nums = 0
odd_nums = 0

num = int(input("Введите натуральное число: "))

while True:
    if num % 10 % 2:
        odd_nums += 1
    else:
        even_nums += 1

    num //= 10

    if not num:
        break

print(f"четных {even_nums} нечетных {odd_nums}")