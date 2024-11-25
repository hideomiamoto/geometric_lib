import math


def area(r):
    '''
    Возвращает площадь окружности

        Принимает на вход десятичное число r (int), возвращает πr²
    '''
    if r < 0:
        raise ValueError("Radius can't be negative or zero")

    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности

        Принимает на вход десятичное число r (int), возвращает 2πr
    '''
    if r < 0:
        raise ValueError("Radius can't be negative or zero")

    return 2 * math.pi * r
