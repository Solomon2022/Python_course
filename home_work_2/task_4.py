# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

str_user = input("Введите строку: ")
i = 1
for el in str_user.split():
    print(f"{i}) {el[:10]}")
    i += 1
