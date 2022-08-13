# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt', 'r', encoding='utf-8') as f:
    name_list = []
    salary_list = []
    for el in f:
        name, salary = el.split()
        salary = float(salary)
        salary_list.append(salary)
        if salary < 20_000:
            name_list.append(name)

    print('Сотрудники имеющие оклад менее 20 тысяч:\n', name_list)
    print('Средний доход сотрудников: \n', sum(salary_list) / len(salary_list))
