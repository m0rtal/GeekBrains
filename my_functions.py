def get_digit_from_user(text="Введите число: "):
    """Используя текст запроса, повторяет запрос на ввод числа до тех пор, пока оно не будет введено.
    Возвращает введённое число в формате float."""
    number = ""
    while not number.lstrip("-").replace(".", "").isdigit():
        number = input(text)
    return float(number)
