# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться
# к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

general_sum = 0


def summation(numbers, sum_f):
    for el in numbers:
        print(f'+{el}')
        sum_f += el
        print(f'={sum_f}')
    return sum_f


while True:
    user_input = (input('Введите числа через пробел (Выход "q"): '))
    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        if user_input.find('q') != -1:
            my_list = user_input.split('q')
            summation(list(map(int, my_list[0].split())), general_sum)
            print('Выход')
            break
        else:
            print('Введены некорректные данные!')
    else:
        general_sum = summation(numbers, general_sum)
