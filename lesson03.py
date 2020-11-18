from my_functions import get_digit_from_user


# Задание 01
def divide(x, y):
    return x / y if y != 0 else print("Деление на 0 не возможно!")


print(divide(get_digit_from_user(), get_digit_from_user()))


# Задание 02
def get_user_info(name, surname, year, city, email, phone):
    return f"{name} {surname}, {year}, living in {city} city, email {email}, phone {phone}"


print(get_user_info(name="Peter", surname="Jacobson", year=1900, city="Default", email="no@bo.dy", phone="+1234567890"))


# Задание 03
def greatest_sum(a, b, c):
    values = [a, b, c]
    values.remove(min(values))
    return sum(values)


print(greatest_sum(1, 2, 3))


# Задание 04
def my_func(x, y):
    y = int(y)
    result = 1
    for _ in range(abs(y)):
        result /= x
    return result


x = get_digit_from_user("Введите х: ")
y = get_digit_from_user("Введите y: ")
print(my_func(x, y))

# Задание 05
summ = 0
stop = "q"
quit = False
while not quit:
    user_input = input("Введите ряд чисел через пробел и q для выхода: ").lower()
    if stop not in user_input:
        numbers = user_input.split()
        summ += sum([int(number) for number in numbers])
        print(f"Сумма введённых чисел: {summ}")
    else:
        user_input = user_input.replace(stop, "")
        numbers = user_input.split()
        summ += sum([int(number) for number in numbers])
        print(f"Сумма введённых чисел: {summ}")
        quit = True


# Задание 06
def int_func(word):
    return word.capitalize()


print(int_func("test"))


def int_func2(sentence):
    return " ".join([int_func(word) for word in sentence.split()])


print(int_func2("test test test"))
