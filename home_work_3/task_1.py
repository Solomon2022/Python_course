# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_number(number_1, number_2):
    """Возвращает результат деления."""

    """позиционные аргументы:
    number_1 - делимое
    number_2 - делитель
    number_1 / number_2 -> return
    """
    return number_1 / number_2


number_user1 = int(input('Введите делимое: '))
number_user2 = int(input('Введите делитель: '))
try:
    print('Результат деления: ', round(division_number(number_user1, number_user2), 2))
except ZeroDivisionError:
    print('Деление на ноль!')
