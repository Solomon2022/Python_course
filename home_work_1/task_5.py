# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчёте на одного сотрудника.

revenue = float(input("Введите сумму выручки: "))
costs = float(input("Введите сумму издержек: "))
profit = revenue - costs
if profit < 0:
    print("Фирма работает в минус!")
elif profit == 0:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в плюс!")
    print(f"Рентабельность фирмы состовляет: {profit / revenue * 100:.2f} %")
    worker = int(input("Введите количество сотрудников: "))
    print(f"Средняя зарплата сотрудников: {profit / worker:.2f}")