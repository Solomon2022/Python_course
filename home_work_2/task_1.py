# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не
# запрашивать у пользователя, а указать явно, в программе.

my_list = [2, 'text', 43.5, None, False, [1, 2]]
print("Мой список: ", my_list)
j = 1
for el in my_list:
    print(f"{j}) {el} - type: {type(el)}")
    j += 1
