import math


def area_circle(r):
    '''
    Возвращает площадь окружности

        Принимает на вход десятичное число r (int), возвращает πr²
    '''
    return math.pi * r * r


def perimeter_circle(r):
    '''
    Возвращает периметр окружности

        Принимает на вход десятичное число r (int), возвращает 2πr
    '''
    return 2 * math.pi * r

