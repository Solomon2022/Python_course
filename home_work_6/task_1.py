# 1. Создать класс TrafficLight (светофор).
# Определить у него один атрибут color(цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
import turtle


def position(x, y):
    """Переносит черепашку на позицию x, y без рисования"""
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()


def clean_color():
    """Перекрашивает круги сфетофора в белый цвет"""
    y = 140
    for i in range(3):
        position(20, y)
        turtle.begin_fill()
        turtle.fillcolor("white")
        turtle.circle(80)
        turtle.end_fill()
        y -= 160


def draw_color(color):
    """Закрашивает один из кругов сфетовора"""
    if color == 'red':
        position(20, 140)
    elif color == 'yellow':
        position(20, -20)
    elif color == 'green':
        position(20, -180)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(80)
    turtle.end_fill()


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self, n):
        for i in range(n):
            for el in self.__color:
                if el == 'красный':
                    clean_color()
                    draw_color('red')
                    time.sleep(7)
                elif el == 'желтый':
                    clean_color()
                    draw_color('yellow')
                    time.sleep(2)
                else:
                    clean_color()
                    draw_color('green')
                    time.sleep(5)


position(-80, 300)
turtle.pensize(5)
turtle.speed(8)
for i in range(2):
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(480)
    turtle.right(90)
y = 140
for i in range(3):
    position(20, y)
    turtle.circle(80)
    y -= 160
turtle.speed(0)

a = TrafficLight()
a.running(2)
