# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first = input("Введите первую букву: ")
second = input("Введите вторую букву: ")

start = ord("a")-1
position1 = ord(first) - start
position2 = ord(second) - start
print(f"{first} - {position1}-я буква в алфавите")
print(f"{second} - {position2}-я буква в алфавите")
difference = abs(position1-position2)-1
print(f"Между буквами {first} и {second} - {difference} букв")
