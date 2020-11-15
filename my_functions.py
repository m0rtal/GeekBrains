def get_digit_from_user(text="Введите число: "):
    number = ""
    while not number.lstrip("-").replace(".", "").isdigit():
        number = input(text)
    return float(number)
