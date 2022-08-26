# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_list = []

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def expence_textile(self):
        pass

    @property
    def sum_expence(self):
        return sum(self.sum_list)


class Overcoat(Clothes):
    @property
    def expence_textile(self):
        result = round(self.size / 6.5 + 0.5, 2)
        self.sum_list.append(result)
        return result


class Costume(Clothes):
    @property
    def expence_textile(self):
        result = self.size * 2 + 0.3
        self.sum_list.append(result)
        return result


a = Overcoat(10)
print(a.expence_textile)

b = Costume(8)
print(b.expence_textile)

print(a.sum_list)
print(a.sum_expence)
