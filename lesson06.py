# # Задание 01
# from itertools import cycle
# from time import sleep
#
#
# class TrafficLight:
#     __color = [["красный", [7, 31]], ["жёлтый", [2, 33]], ["зелёный", [5, 32]], ["жёлтый", [2, 33]]]
#
#     def running(self):
#         count = 0
#         for light in cycle(self.__color):
#             if count > 6:
#                 break
#             print(f"\r\033[{light[1][1]}m{light[0]}", end="")
#             sleep(light[1][0])
#
#             count += 1
#
#
# tl = TrafficLight()
# tl.running()
#
# # Задача 02
# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calculate_mass(self):
#         return f"{self._width}м * {self._length}м * 25кг * 5см = {(self._length * self._width * 25 * 5) / 1000:.0f}т"
#
#
# road = Road(length=5000, width=20)
# print(road.calculate_mass())
#
#
# Задача 03
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    @property
    def income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


employee1 = Position("Иван", "Иванов", "принеси", 10000, 5000)
print(employee1.name)
print(employee1.surname)
print(employee1.position)
print(employee1.income)
print(employee1.get_full_name())
print(employee1.get_total_income())
