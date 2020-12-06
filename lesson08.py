# class Date:
#     def __init__(self, date_str):
#         """должна принимать дату в виде строки формата «день-месяц-год»"""
#         if isinstance(date_str, str):
#             self.date_str = date_str
#             self.retrieve_date()
#         else:
#             print("Принимает дату в виде строки формата «день-месяц-год»")
#
#     def retrieve_date(self):
#         self.day, self.month, self.year = map(int, self.date_str.split("-"))
#         if self.validate(self.day, self.month, self.year):
#             print("Date is valid")
#         else:
#             print("Date is not valid")
#
#     @staticmethod
#     def validate(day, month, year):
#         if day in range(1, 32) and month in range(1, 13) and year > 0:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return " ".join(map(str, (self.day, self.month, self.year)))
#
#
# date = Date("11-11-2020")
# print(date)
#
# date = Date("11-13-2020")
# print(date)
#
# date = Date("32-11-2020")
# print(date)
#
#
# # Задание 02
# class DivisionByZeroError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# def division(divisible, divider):
#     """Делит два числа и корректно обрабатывает деление на 0"""
#     try:
#         if divider == 0:
#             raise DivisionByZeroError("Нельзя делить на ноль!")
#     except DivisionByZeroError as err:
#         print(err)
#     else:
#         print(divisible / divider)
#
#
# division(3, 0)
# division(10, 2)
#
#
# # Задание 03
# class NumbersOnly(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# stop_word = "stop"
# my_list = []
# while (inp := input("Введите число или stop для остановки цикла: ")) != stop_word:
#     try:
#         if not inp.isdigit():
#             raise NumbersOnly("Допустимы только числа!")
#         my_list.extend(inp)
#     except NumbersOnly as err:
#         print(err)
#
# print(f"Сформированный список: {my_list}")

# Задание 04
