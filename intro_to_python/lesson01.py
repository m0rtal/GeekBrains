# Задание 1

digit = 1
my_list = [digit, "ещё что-то", "ещё что-то"]
my_dict = {"key": my_list}
my_set = set(my_list)
my_tuple = (1, 2, 3)

name = input("Введите имя: ")
print(f"Введённое имя: {name}")
x = float(input("Давайте возведём число в квадрат: ")) ** 2
print(f"А вот и квадрат: {x}")

# Задание 2
user_time = float(input("Введите время в секундах: "))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = (user_time - hours * 3600 - minutes * 60) % 60

print("Оно же в чч:мм:сс: %02d:%02d:%02d" % (hours, minutes, seconds))

# Задание 3
n = int(input("Введите n, будет фокус: "))
print("n + nn + nnn = %d" % (n + (n * 11) + (n * 111)))

# Задание 4
number = input("Введите целое положительно число: ")
maximum = 0
digits = len(number) - 1
while digits >= 0:
    if int(number[digits]) > maximum:
        maximum = int(number[digits])
    digits -= 1
print(f"Самая большая цифра в этом числе - {maximum}")

# Задание 5
revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if costs > revenue:
    print("Фирма работает в убыток")
elif costs < revenue:
    print("Фирма работает с прибылью")
    print("Рентабельность: %.2f" % (revenue / costs))
    staff = int(input("Введите количество сотрудников фирмы: "))
    print("Прибыль фирмы в расчёте на одного сотрудника: %.2f" % ((revenue - costs) / staff))

# Задание 6
a = int(input("Введите результат спортсмена в первый день: "))
b = int(input("Введите ожидаемый показатель спортсмена: "))
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f"На {day}-й день спортсмен достиг результата — не менее {b} км.")
