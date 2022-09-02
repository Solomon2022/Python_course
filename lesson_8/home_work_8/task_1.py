# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import datetime


class Data:
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def converter(cls, data_str):
        return (list(map(int, data_str.split('-'))))

    @staticmethod
    def validate(data_list):
        data_list = Data.converter(data_list)
        check = None
        try:
            new_data = datetime.datetime(data_list[2], data_list[1], data_list[0])
            check = True
        except ValueError:
            check = False
        return check


print(Data.converter('12-02-2012'))
d = Data('12-12-12')
print(d.validate('12-12-12'))
