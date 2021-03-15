def binary_search(lst: list, item: int) -> (int, int):
    """
    :param lst: список чисел
    :param item: заданное к поиску число
    :return: вернёт позицию задданого числа в списке
    """
    index_low = 0
    index_high = len(lst) + 1

    # на всякий случай сортируем список
    lst.sort()
    steps = 0
    while index_low <= index_high:
        index_middle = int((index_low + index_high) / 2)
        guess = lst[index_middle]
        if guess == item:
            return index_middle, steps
        if guess > item:
            index_high = index_middle - 1
            steps += 1
        else:
            index_low = index_middle + 1
            steps += 1
    return None, None


my_list = list(range(0, 1000, 1))
number = 7

position, steps = binary_search(my_list, number)
print(f"Число {number} найдено за {steps} шага(ов) на {position}-й позиции в спике") if position else print(
    "Число не найдено в списке")
