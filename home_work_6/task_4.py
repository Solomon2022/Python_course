# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')

    def show_speed(self):
        print(f'Текущая скорость машины {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Скорость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Скорость превышена!')


class PoliceCar(Car):
    pass


a = TownCar(70, 'Красный', 'Mazda', False)
b = SportCar(150, 'Желтый', 'Ferarri', False)
c = WorkCar(30, 'Черный', 'Зил', False)
d = PoliceCar(90, 'Бело-синий', 'Ford', True)

print(f'Машина:{a.name}, Цвет: {a.color}, Скорость: {a.speed}, Принадлежность к полиции: {a.is_police}')
a.go()
a.stop()
a.turn('Лево')
a.show_speed()

print(f'\n Машина:{b.name}, Цвет: {b.color}, Скорость: {b.speed}, Принадлежность к полиции: {b.is_police}')
b.go()
b.stop()
b.turn('Лево')
b.show_speed()

print(f'\n Машина:{c.name}, Цвет: {c.color}, Скорость: {c.speed}, Принадлежность к полиции: {c.is_police}')
c.go()
c.stop()
c.turn('Лево')
c.show_speed()

print(f'\n Машина:{d.name}, Цвет: {d.color}, Скорость: {d.speed}, Принадлежность к полиции: {d.is_police}')
d.go()
d.stop()
d.turn('Лево')
d.show_speed()
