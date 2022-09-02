# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные
# для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
# определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


def help_cm():  # Функция help (список команд)
    print('\nСписок команд:')
    print('create_storege - создание склада;')
    print('create_equipment - создание оргтехники;')
    print('create_department - создание подразделений;')
    print('print_storege - cписок всех складов;')
    print('unpack_storege - посмотреть содержимое склада;')
    print('print_department - cписок всех подразделений;')
    print('unpack_department - посмотреть содержимое подразделения;')
    print('moving - перемещение оргтехники')

    print('exit - выход из программы;')


def isdigit_number():
    while True:
        number = input('введите число: ')
        if number.isdigit() and number != '0':
            number = int(number)
            return number
            break
        else:
            print('Число должно быть положительным и целым!')


def isdigit_number_2():
    while True:
        number = input('введите число: ')
        if number.isdigit():
            number = int(number)
            return number
            break
        else:
            print('Число должно быть положительным и целым!')


def create_storege():  # Функция собирает инфу для создания склада
    while True:
        name = input('Введите название склада: ')
        if name in dict_storege:
            print('Склад с таким именем уже существует!')
        else:
            break
    print('Вместимость склада ', end='')
    max_storege = isdigit_number()
    return name, max_storege


def create_department():
    while True:
        name = input('Введите название подразделения: ')
        if name in dict_department:
            print('Подразделение с таким именем уже существует!')
        else:
            break
    return name


def print_storege():  # Функция печатает список складов
    print('Список всех складов:')
    if not dict_storege:
        print('вы не создали ни одного склада')
    else:
        i = 1
        for key in dict_storege:
            print(f'{i}) Склад "{key}" вместимость: {dict_storege[key].max_storege}')
            i += 1


def print_department():  # Функция печатает список подразделений
    print('Список всех подразделений:')
    if not dict_department:
        print('вы не создали ни одного подразделения')
    else:
        i = 1
        for key in dict_department:
            print(f'{i}) Подразделение "{key}"')
            i += 1


def create_equipment_1():  # Функция собирает инфу для создания принтера сканера или ксерокса
    if not dict_storege:
        print('Для создания оргтехники необходимо создать хотябы один склад')
    else:
        name_storege = choice_storege()
        while True:
            type_equipment = input('Для создания Принтера введите - 1, Сканер - 2, Ксерокс - 3: ')
            if type_equipment == '1':
                print('Создаем Принтеры: ')
                type_equipment = 'Принтер'
                break
            elif type_equipment == '2':
                print('Создаем Сканеры: ')
                type_equipment = 'Сканер'
                break
            elif type_equipment == '3':
                print('Создаем Ксероксы: ')
                type_equipment = 'Ксерокс'
                break
            else:
                print('Неизветсная команда!')
        create_equipment_2(name_storege, type_equipment)


def create_equipment_2(name_storege,
                       type_equipment):  # Функция продолжает собирать инфу для создания принтера сканера или ксерокса
    model = input('Введите модель (например: Sumsung-1200): ')
    print('Задайте цену ', end='')
    price = isdigit_number()
    if type_equipment == 'Принтер':
        while True:
            format_or_color = input('Введите "1" - если принтер цветной и "2" - черно-белый: ')
            if format_or_color in ['1', '2']:
                break
            else:
                print('Неизветсный параметр!')
    else:
        while True:
            format_or_color = input('Введите формат усройства(например A1): ')
            if format_or_color in ['A1', 'A2', 'A3', 'A4', 'A5']:
                break
            else:
                print('Неизветсный формат!')
    while True:
        print('Задайте количество ', end='')
        quantity = isdigit_number()
        loose_storege = dict_storege[name_storege].max_storege - dict_storege[name_storege].quantity_storege
        if loose_storege < quantity:
            print(f'Недостаточно места! Склад "{name_storege}" вместимость {dict_storege[name_storege].max_storege}')
            print(f'Свободно: {loose_storege}, необходимо: {quantity}')
        else:
            break

    create_equipment_3([name_storege, quantity, type_equipment, model, price, format_or_color])


def create_equipment_3(parameters):  # Функция создает объект принтер, сканер или ксерокс
    name_storege = parameters[0]
    storege_obj = dict_storege[name_storege]
    quantity = parameters[1]
    type_equipment = parameters[2]
    model = parameters[3]
    price = parameters[4]
    format_or_color = parameters[5]
    if type_equipment == 'Принтер':
        type_class = Printer
    elif type_equipment == 'Сканер':
        type_class = Scanner
    elif type_equipment == 'Ксерокс':
        type_class = Copier

    storege_obj.quantity_storege += quantity
    for i in range(quantity):
        obj = type_class(type_equipment, model, price, format_or_color)
        storege_obj.storege[type_equipment].append(obj)
    unpack_storege(name_storege)


def unpack_storege(name_storege=False):  # функция выводит содержимое выбранного склада
    if not dict_storege:
        print('Для просмотра склада необходимо создать хотябы один')
    else:
        if not name_storege:
            name_storege = choice_storege()
        print(f'Склад {name_storege}:')
        print(dict_storege[name_storege])


def unpack_department(name_department=False):  # функция выводит содержимое выбранного подразделения
    if not dict_department:
        print('Для просмотра подразделения необходимо создать хотябы одино')
    else:
        if not name_department:
            name_department = choice_department()
        print(f'Подразделение {name_department}:')
        print(dict_department[name_department])


def choice_department():  # Функция нахождения и выбора нужного подразделеня
    print('Выберете подразделение:')
    print_department()
    while True:
        name_department = input('Введите имя подразделения: ')
        if not name_department in dict_department:
            print(f'Подразделение с именем "{name_department}" не существет')
            print_department()
        else:
            print(f'Выбрано подразделение "{name_department}"\n')
            break
    return name_department


def choice_storege():  # Функция нахождения и выбора нужного склада
    print('Выберите склад:')
    print_storege()
    while True:
        name_storege = input('Введите имя склада: ')
        if not name_storege in dict_storege:
            print(f'Склада с именем "{name_storege}" не существет')
            print_storege()
        else:
            print(f'Выбран склад "{name_storege}"\n')
            break
    return name_storege


def quantity_equipment():
    print('Задайте количество принтеров:')
    printer_quantity = isdigit_number_2()
    print('Задайте количество сканеров:')
    scanner_quantity = isdigit_number_2()
    print('Задайте количество ксероксов:')
    copier_quantity = isdigit_number_2()
    return [printer_quantity, scanner_quantity, copier_quantity]


def moving():  # функция перемещения оборудования
    if not dict_storege or not dict_department:
        print('Для перемещения необходимо создать хотябы одно оборудование и одно подразделение')
    else:
        name_storege = choice_storege()
        obj_storege = dict_storege[name_storege]
        name_department = choice_department()
        obj_department = dict_department[name_department]
        unpack_storege(name_storege)
        unpack_department(name_department)
        while True:
            type_moving = input('Выберете режим перемещения: 1 - склад->подразделение, 2 - подразделение->склад: ')
            if type_moving == '1':
                print(f'Перемещаем из склада "{name_storege}" в подразделение {name_department}!')
                obj_storege.moving_storege_department(obj_department, name_storege, name_department)
                break
            elif type_moving == '2':
                print(f'Перемещаем из подразделения "{name_department}" на склад {name_storege}!')
                obj_department.moving_department_storege(obj_storege, name_storege, name_department)
                break
            else:
                print('Неизветсная команда!')


class Storehouse:
    def __init__(self, max_storege):
        self.storege = {'Принтер': [],
                        'Сканер': [],
                        'Ксерокс': []}
        self.max_storege = max_storege
        self.quantity_storege = 0

    def __str__(self):
        my_str = ''
        for el in self.storege:
            my_str += (f'{el} - {len(self.storege[el])}\n')
        return (f'Вместимость: {self.max_storege}, заполнен: {self.quantity_storege} \n{my_str}')

    def moving_storege_department(self, other_department, name_storege, name_department):
        while True:
            my_list = list(map(int, quantity_equipment()))
            printer_quantity = my_list[0]
            scanner_quantity = my_list[1]
            copier_quantity = my_list[2]
            if printer_quantity > len(self.storege['Принтер']) or scanner_quantity > len(
                    self.storege['Сканер']) or copier_quantity > len(self.storege['Ксерокс']):
                print('На складе нет достаточного количества оборудования')
            else:
                break
        self.quantity_storege -= sum(my_list)
        for i in range(printer_quantity):
            other_department.equipment['Принтер'].append(self.storege['Принтер'][0])
            self.storege['Принтер'].pop(0)
        for i in range(scanner_quantity):
            other_department.equipment['Сканер'].append(self.storege['Сканер'][0])
            self.storege['Сканер'].pop(0)
        for i in range(copier_quantity):
            other_department.equipment['Ксерокс'].append(self.storege['Ксерокс'][0])
            self.storege['Ксерокс'].pop(0)
        unpack_storege(name_storege)
        unpack_department(name_department)


class Department:
    def __init__(self):
        self.equipment = {'Принтер': [],
                          'Сканер': [],
                          'Ксерокс': []}

    def __str__(self):
        my_str = ''
        for el in self.equipment:
            my_str += (f'{el} - {len(self.equipment[el])}\n')
        return my_str

    def moving_department_storege(self, other_storege, name_storege, name_department):
        while True:
            my_list = list(map(int, quantity_equipment()))
            printer_quantity = my_list[0]
            scanner_quantity = my_list[1]
            copier_quantity = my_list[2]
            if printer_quantity > len(self.equipment['Принтер']) or scanner_quantity > len(
                    self.equipment['Сканер']) or copier_quantity > len(self.equipment['Ксерокс']):
                print('В подразделении нет достаточного количества оборудования')
            else:
                break
        other_storege.quantity_storege += sum(my_list)
        for i in range(printer_quantity):
            other_storege.storege['Принтер'].append(self.equipment['Принтер'][0])
            self.equipment['Принтер'].pop(0)
        for i in range(scanner_quantity):
            other_storege.storege['Сканер'].append(self.equipment['Сканер'][0])
            self.equipment['Сканер'].pop(0)
        for i in range(copier_quantity):
            other_storege.storege['Ксерокс'].append(self.equipment['Ксерокс'][0])
            self.equipment['Ксерокс'].pop(0)
        unpack_storege(name_storege)
        unpack_department(name_department)


class OfficeEquipment:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        # storehouse.input_equipment(self)


class Printer(OfficeEquipment):
    def __init__(self, type, model, price, color):
        super().__init__(type, model, price)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, type, model, price, format):
        super().__init__(type, model, price)
        self.format = format


class Copier(OfficeEquipment):
    def __init__(self, type, model, price, format):
        super().__init__(type, model, price)
        self.format = format


# ___________________________________________________________________________________________________________

print('\nПрограмма для отслеживания принтеров, сканеров, ксероксов в компании!\n')
print('Для просмотра списка команд введиет: help\n')

a = Storehouse(50)
b = Department()

dict_storege = {'aaa': a}
dict_department = {'bbb': b}

while True:
    command = input('Введите команду: ')
    if command == 'exit':
        break
    elif command == 'help':
        help_cm()
    elif command == 'create_storege':
        value_typle = create_storege()
        dict_storege[value_typle[0]] = Storehouse(value_typle[1])
        print(f'Склад {value_typle[0]} с вместимостью {value_typle[1]} создан')
    elif command == 'create_equipment':
        create_equipment_1()
    elif command == 'create_department':
        name = create_department()
        dict_department[name] = Department()
        print(f'Подразделение {name} создано')
    elif command == 'print_storege':
        print_storege()
    elif command == 'unpack_storege':
        unpack_storege()
    elif command == 'print_department':
        print_department()
    elif command == 'unpack_department':
        unpack_department()
    elif command == 'moving':
        moving()
    else:
        print('Неизветсная команда!')
    print()
