# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input("Введите номер буквы в алфавите: "))
start = ord("a") - 1
print(f"{letter_number}-я буква в алфавите - это {chr(letter_number + start)}")
