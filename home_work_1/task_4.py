# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_user = int(input("Введите целое положительное число: "))
number_max = 0
while number_user != 0:
    number_last = number_user % 10
    if number_max < number_last:
        number_max = number_last
    number_user //= 10
print(f"Максимальная цифра : {number_max}")
