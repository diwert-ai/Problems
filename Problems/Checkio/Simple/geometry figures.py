# https://py.checkio.org/ru/mission/geometry-figures/
import math


class Parameters:
    def __init__(self, param):
        self.param = param
        self.figure = None

    def choose_figure(self, figure):
        self.figure = figure

    def perimeter(self):
        return round(self.figure.perimeter(self.param), 2)

    def area(self):
        return round(self.figure.area(self.param), 2)

    def volume(self):
        return round(self.figure.volume(self.param), 2)


class Circle:
    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

    @staticmethod
    def area(radius):
        return math.pi * radius**2

    @staticmethod
    def volume(radius):
        return 0


class Triangle:
    @staticmethod
    def perimeter(side):
        return 3 * side

    @staticmethod
    def area(side):
        return 3**0.5 * side**2 / 4

    @staticmethod
    def volume(side):
        return 0


class Square:
    @staticmethod
    def perimeter(side):
        return 4 * side

    @staticmethod
    def area(side):
        return side**2

    @staticmethod
    def volume(side):
        return 0


class Pentagon:
    @staticmethod
    def perimeter(side):
        return 5 * side

    @staticmethod
    def area(side):
        return side**2 * (25 + 10 * 5**0.5)**0.5 / 4

    @staticmethod
    def volume(side):
        return 0


class Hexagon:
    @staticmethod
    def perimeter(side):
        return 6 * side

    @staticmethod
    def area(side):
        return 3 * side**2 * 3**0.5 / 2

    @staticmethod
    def volume(side):
        return 0


class Cube:
    @staticmethod
    def perimeter(side):
        return 12 * side

    @staticmethod
    def area(side):
        return 6 * side**2

    @staticmethod
    def volume(side):
        return side**3


def test0():
    figure = Parameters(10)
    figure.choose_figure(Circle())
    print(figure.area())
    figure.choose_figure(Triangle())
    print(figure.perimeter())


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")


def test2():
    figure = Parameters(10)
    figure.choose_figure(Pentagon())
    print(figure.area())


if __name__ == '__main__':
    test0()
    test1()
    test2()
