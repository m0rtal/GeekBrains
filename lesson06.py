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
# # Задача 03
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#     @property
#     def income(self):
#         return self._income
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f"Сотрудник: {self.name} {self.surname}"
#
#     def get_total_income(self):
#         return sum(self.income.values())
#
#
# employee1 = Position(name="Иван", surname="Иванов", position="принеси-подай", wage=10000, bonus=5000)
# print(employee1.name)
# print(employee1.surname)
# print(employee1.position)
# print(employee1.income)
# print(employee1.get_full_name())
# print(employee1.get_total_income())
#
# # Задача 04
# NORMALIZE_TEXT = "\033[0m"
#
#
# class Car:
#     def __init__(self, color, name, speed=0):
#         self.speed = speed
#         self._color = color
#         self.name = name
#         self._is_police = False
#
#     def is_police(self):
#         if self._is_police:
#             return "Это полицейская машина"
#         else:
#             return "Это гражданская машина"
#
#     def color(self):
#         return f"Цвет автомобиля {self.name} - {self._color}"
#
#     def go(self):
#         return NORMALIZE_TEXT + f"Машина {self.name} поехала"
#
#     def stop(self):
#         self.speed = 0
#         return NORMALIZE_TEXT + f"Машина {self.name} остановилась"
#
#     def turn(self, direction):
#         return NORMALIZE_TEXT + f"Машина {self.name} повернулась в направлении {direction}"
#
#     def show_speed(self):
#         if self.speed > 0:
#             return NORMALIZE_TEXT + f"Скорость {self.name} - {self.speed}км/ч"
#         elif self.speed == 0:
#             return NORMALIZE_TEXT + f"Машина {self.name} стоит на месте"
#         else:
#             return NORMALIZE_TEXT + f"У машины что-то не так со скоростью"
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f"\033[31mСкорость {self.name} - {self.speed}км/ч, машина едет с превышением!"
#         else:
#             return super().show_speed()
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f"\033[31mСкорость {self.name} - {self.speed}км/ч, машина едет с превышением скорости!"
#         else:
#             return super().show_speed()
#
#
# class PoliceCar(Car):
#     def __init__(self, color, name, speed=0):
#         super().__init__(color, name, speed)
#         self._is_police = True
#
#
# def show_all(object, direction):
#     """Проходит по всем атрибутам и методам класса, показывая их работоспособность"""
#     print("-" * 80)
#     print(object.color())
#     print(object.is_police())
#     print(object.go())
#     print(object.speed)
#     print(object.show_speed())
#     print(object.turn(direction))
#     print(object.stop())
#     print(object.show_speed())
#
#
#
# town_car = TownCar("чёрный", "Prius", 80)
# show_all(town_car, "налево")
#
# sport_car = SportCar("красный", "Lambo", 80)
# show_all(sport_car, "направо")
#
# work_car = WorkCar("жёлтый", "Ларгус", 50)
# show_all(work_car, "на север")
#
# police_car = PoliceCar("чёрно-белый", "Ford Fairlane Crown Victoria", 120)
# show_all(police_car, "за нарушителем")
#
#
# Задача 05
