# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def person_info(name, lastname, year, city, email, phone):
    print(f'{name} {lastname}, {year} г.р., г. {city}, email: {email}, телефон: {phone}')


person_info(name='Max', lastname='Orlov', year=1990, city='Moscow', email='12345@mail.ru', phone=1230404043)
