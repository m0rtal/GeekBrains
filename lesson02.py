# # Задание 01
# my_list = [1, "a", {"key": "value"}, [0, 1], (0, 1), set("test"), True, None]
#
# for element in my_list:
#     print(type(element))

# # Задание 02
# shuffle_list = input("Введите любое количество чиселе через пробел: ").split()
# length = len(shuffle_list)
# counter = 1
# while counter < length:
#     shuffle_list[counter], shuffle_list[counter - 1] = shuffle_list[counter - 1], shuffle_list[counter]
#     counter += 2
# print("Перемешанный список: ", shuffle_list)

# # Задание 03
# month = int(input("Введите номер месяца: "))
# monthes = ["зима", "весна", "лето", "осень", "зима"]
# print(monthes[month // 3])
#
# year = {"зима": (1, 2, 12), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
# for key in year.keys():
#     if month in year[key]:
#         print(key)

# # Задание 04
# sentence = input("Введите несколько слов через пробел: ").split()
# for index, word in enumerate(sentence):
#     print(index, word[:10])

# # Задание 05
# rating = [7, 5, 3, 3, 2]
# print(rating)
# user_input = int(input("Введите новое число: "))
# if user_input in rating:
#     rating.insert(rating.index(user_input)+1, user_input)
# elif user_input < rating[-1]:
#     rating.append(user_input)
# elif user_input > rating[0]:
#     rating.insert(0, user_input)
# else:
#     for i in range(len(rating)):
#         if user_input < rating[i] and user_input > rating[i+1] :
#             rating.insert(rating.index(rating[i])+1, user_input)
# print(rating)

# Задание 06
sklad = []
positions = int(input("Введите количество позиций: "))
for i in range(1, positions + 1):
    name = input(f"Название {i} позиции: ")
    price = float(input("Её цена: "))
    pcs = float(input("Количество: "))
    measure = input("Единицы измерения: ")
    sklad.append((i, {"название": name, "цена": price, "количество": pcs, "ед": measure}))

print("Позиции на складе")
for item in sklad:
    print(item)

print("ЕНебольшая аналитика по товарам: ")
analytics = []
for key in sklad[0][1].keys():
    values = set([item[1][key] for item in sklad])
    analytics.append({key: values})

print(analytics)