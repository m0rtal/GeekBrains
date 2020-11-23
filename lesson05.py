# Задание 01
# filename = "text.txt"
# text = input("Введите текст для сохранения: ")
# while text != "":
#     with open(filename, "a", encoding="utf-8") as fha:
#         fha.write(text + "\n")
#     text = input("Введите текст для сохранения: ")
#
# # задание 02
# with open(filename, "r", encoding="utf-8") as fhr:
#     text = fhr.readlines()
#
# print(f"В считанном файле {filename} было строк: {len(text)}, слов: {sum([len(line.split()) for line in text])}")
#
# # Задание 03
# import string
# from random import choice, randint, random
# from math import fsum
#
#
# def randomletters():
#     """Генерирует случайный набор символов случайной длины"""
#     # letters = string.ascii_lowercase  # хотел латинскими, но это скучно
#     letters = "".join([chr(i) for i in range(ord('а'), ord('а') + 32)])
#     length = randint(5, 15)
#     return "".join(choice(letters) for _ in range(length)).capitalize()
#
#
# def randomsalary():
#     """Генерирует случайное float число в диапазоне от ~1.000 до ~200.000"""
#     salary = random() * randint(100000, 200000)
#     return round(salary, 2)
#
#
# # Сгенерируем файл с зарплатой
# filename = "salary.txt"
# for _ in range(100):
#     with open(filename, "a") as fha:
#         fha.write(f"{randomletters()} {randomsalary()}\n")
#
# with open(filename, "r") as fhr:
#     salary = fhr.readlines()
#
# poverty = [line.split()[0] for line in salary if float(line.split()[1]) < 20000]
# print("Сотрудники, которым срочно нужно поднять зарплату:\n", "\n".join(poverty), sep="")
#
#
# total_salary = fsum([float(line.split()[1]) for line in salary])
# poverty_salaries_list = [float(line.split()[1]) for line in salary if float(line.split()[1]) < 20000]
# poverty_salary = fsum(poverty_salaries_list)
# print(f"Средняя зарплата персонала: {(total_salary / len(salary)):.2f}")
# print(f"Средняя зарплата нуждающегося персонала: {(poverty_salary / len(poverty_salaries_list)):.2f}")
#
# # Задание 04
# from translate import Translator
#
# translator = Translator(from_lang="English", to_lang="Russian")
#
# with open("four.txt", "r") as fhr:
#     text_list = fhr.readlines()
#
# for line in text_list:
#     words = line.split()
#     words[0] = translator.translate(words[0])
#     words = " ".join(words) + "\n"
#     with open("четыре.txt", "a") as fha:
#         fha.write(words)
#
# # Задание 05
# filename = "numbers.txt"
# numbers = " ".join([str(randint(0, 9)) for _ in range(1000)])
# with open(filename, "a") as fha:
#     fha.write(numbers)
#
# with open(filename, "r") as fhr:
#     text = fhr.read()
#
# print(f"Сумма чисел в файле {filename}: {fsum([float(number) for number in text.split()]):.0f}")
#
# Задание 06

