# Задание 01
filename = "text.txt"
text = input("Введите текст для сохранения: ")
while text:
    with open(filename, "a", encoding="utf-8") as fha:
        fha.write(text + "\n")
    text = input("Введите текст для сохранения: ")

# задание 02
with open(filename, "r", encoding="utf-8") as fhr:
    text = fhr.readlines()

print(f"В считанном файле {filename} было строк: {len(text)}, слов: {sum([len(line.split()) for line in text])}")

# Задание 03

from random import choice, randint, random

from math import fsum


def randomletters():
    """Генерирует случайный набор символов русского алфавита случайной длины от 5 до 15 символов"""
    # letters = string.ascii_lowercase  # хотел латинскими, но это скучно
    letters = "".join([chr(i) for i in range(ord('а'), ord('а') + 32)])
    length = randint(5, 15)
    return "".join(choice(letters) for _ in range(length)).capitalize()

def randomsalary():
    """Генерирует случайное float число в диапазоне от ~1.000 до ~200.000"""
    salary = random() * randint(100000, 200000)
    return round(salary, 2)


filename = "salary.txt"
for _ in range(100):
    with open(filename, "a", encoding="utf-8") as fha:
        fha.write(f"{randomletters()} {randomsalary()}\n")

with open(filename, "r", encoding="utf-8") as fhr:
    salaries = {row.split()[0]: float(row.split()[1]) for row in fhr.readlines()}

poverty = {name: salary for name, salary in salaries.items() if salary < 20000}
print("Сотрудники, которым срочно нужно поднять зарплату:", "\n".join(poverty), sep="\n")

print(f"Средняя зарплата персонала: {(sum(salaries.values()) / len(salaries)):.2f}")
print(f"Средняя зарплата нуждающегося персонала: {(sum(poverty.values()) / len(poverty)):.2f}")

# Задание 04
from translate import Translator

translator = Translator(from_lang="English", to_lang="Russian")

with open("four.txt", "r", encoding="utf-8") as fhr:
    text_list = fhr.readlines()

for line in text_list:
    words = line.split()
    words[0] = translator.translate(words[0])
    words = " ".join(words) + "\n"
    with open("четыре.txt", "a", encoding="utf-8") as fha:
        fha.write(words)

# Задание 05
filename = "numbers.txt"
numbers = " ".join([str(randint(0, 9)) for _ in range(1000)])
with open(filename, "a", encoding="utf-8") as fha:
    fha.write(numbers)

with open(filename, "r", encoding="utf-8") as fhr:
    text = fhr.read()

print(f"Сумма чисел в файле {filename}: {sum(map(int, text.split())):.0f}")

# Задание 06
from string import punctuation
import re

with open("schedule.txt", "r", encoding="utf-8") as fhr:
    raw_text = fhr.readlines()

schedule = {}
for line in raw_text:
    line = line.translate(str.maketrans("", "", punctuation))
    words = line.split()
    course = words[0]
    # nums = [''.join(filter(str.isdigit, word)) for word in words[1:]]
    nums = re.findall(r'\d+', line)
    summ = sum(int(num) if num else 0 for num in nums)
    schedule[course] = summ

# не пригодилось, но жалко выбрасывать
# records = set(v for key, value in loaded_json.items() for v in value)
# summary = {key: sum(loaded_json[key].values()) for key, value in loaded_json.items()}

for key, value in schedule.items():
    print(f"Общее количество часов по предмету '{key}': {value}")

# Задание 07
import json

ownership = ("ООО", "ИП", "КФХ", "АО", "ЗАО", "ОАО", "ОДО")
firms = "\n".join(
    [" ".join([randomletters(), choice(ownership), str(randint(5000, 20000)), str(randint(5000, 10000))]) for _ in
     range(100)])

filename = "firms.txt"
with open(filename, "w", encoding="utf-8") as fhw:
    fhw.writelines(firms)

with open(filename, "r", encoding="utf-8") as fhr:
    report = {row.split()[0]: (int(row.split()[2]) - int(row.split()[3])) for row in fhr.readlines()}

avg_profit = sum(report.values()) / len(report.values())
print(f"Средняя прибыль без учёта убыточных компаний: {avg_profit}")

new_report = [report, {"average_profit": avg_profit}]

print("Подробно о прибылях компаний:", new_report, sep="\n")

with open("firms.json", "w", encoding="utf-8") as fhw:
    json.dump(new_report, fhw, ensure_ascii=False)
