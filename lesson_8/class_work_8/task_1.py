# Создать произвольную программу о продаже автомобиля от создания до покупателя.
# Автомобиль должен создаваться на заводе и храниться на скаладе

class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class CarFactory:
    model = 'DeLorean'
    common_price = 5500

    def build(self, count=1):
        cars = []
        for i in range(count):
            cars.append(Car(self.model, self.common_price))

        return cars
class CapacityEx(Exception):
    def __init__(self, currend, need):
        self.currend = currend
        self.need = need

    def __str__(self):
        return f'Недостаточно места, необходимо: {self.need}, есть {self.currend}\nНехватает: {self.need - self.currend}'


class CarStock:
    def __init__(self, count=0):
        self.max_count = count
        self.cars = []


    def store(self, cars):

        if len(self.cars) >= self.max_count:
            raise CapacityEx(len(self.cars), len(self.cars) + len(cars))
        self.cars.extend(cars)


class NotEnMoneyEx(Exception):
    def __init__(self, currend, need):
        self.currend = currend
        self.need = need

    def __str__(self):
        return f'Недостаточно денег, необходимо: {self.need}, есть {self.currend}\nНехватает: {self.need - self.currend}'


class Customer:
    def __init__(self, money):
        self.money = money

    def buy(self, car):
        if car.price > self.money:
            raise NotEnMoneyEx(self.money, car.price)
        self.money -= car.price


factory = CarFactory()
stock = CarStock(1)
customer_1 = Customer(1234)

car_list = factory.build(4)
stock.store(car_list)
try:
    customer_1.buy(stock.cars[1])
except NotEnMoneyEx as err:
    print(err)

print(customer_1.money)
