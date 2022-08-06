# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """Принимает три аргумента возвращает сумму наибольших двух аргументов."""

    my_list = [a, b, c]
    print('Ваши числа: ', my_list)
    my_list.remove(min(my_list))
    return sum(my_list), my_list


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

print('Сумма наибольших двух: ', my_func(number_1, number_2, number_3))
