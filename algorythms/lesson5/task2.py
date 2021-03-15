"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’]
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования
систем счисления, задача решается в несколько строк. Для прокачки алгоритмического
мышления такой вариант не подходит. Поэтому использование встроенных функций для
перевода из одной системы счисления в другую в данной задаче под запретом.

Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""

from collections import Counter, OrderedDict
from typing import List

repeat = True
char_offset = 87
base_num = 16


def str2int(char: str):
    return int(char) if char.isnumeric() else (ord(char.lower()) - char_offset)


def int2str(num: int):
    return f"{num}" if 0 <= num <= 9 else chr(num + char_offset)


while repeat:
    a = Counter({i: str2int(c) for i, c in enumerate(reversed(input("Введите первое число: ")))})
    b = Counter({i: str2int(c) for i, c in enumerate(reversed(input("Введите второе число: ")))})
    op = input("Введите оператор: ")

    ranked_terms: List[Counter] = []

    if op == "+":
        ranked_terms = [a, b]
    elif op == "*":
        for offset, value1 in a.items():
            terms = Counter()
            for rank, value2 in b.items():
                rank += offset
                spam = value1 * value2 + terms[rank]
                over, terms[rank] = divmod(spam, base_num)
                if over:
                    terms[rank + 1] += over

            ranked_terms.append(terms)
    else:
        print(f"'{op}': неподдерживаемая операция")
        continue

    result = Counter()

    for terms in ranked_terms:
        for rank, term in terms.items():
            spam = result[rank] + term
            over, result[rank] = divmod(spam, base_num)
            if over:
                result[rank + 1] += over

    print([int2str(i).upper() for i in
           OrderedDict(
               sorted(
                   result.items(),
                   key=lambda x: x[0],
                   reverse=True
               )
           ).values()])

    repeat = input("Повторить? [y/n]: ").lower() == 'y'
