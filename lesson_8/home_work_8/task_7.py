# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    @staticmethod
    def operation_complex(self, other, operation):
        x = complex(self.real, self.imaginary)
        y = complex(other.real, other.imaginary)
        if operation == '+':
            return x + y
        else:
            return x * y

    def __add__(self, other):
        return ComplexNumber.operation_complex(self, other, '+')

    def __mul__(self, other):
        return ComplexNumber.operation_complex(self, other, '*')


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
print(a + b)
print(a * b)
