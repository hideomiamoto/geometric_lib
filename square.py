def area(a):
    '''
    Принимает на вход десятичное число a (int), возвращает площадь квадрата

    '''
    if a <= 0:
        raise ValueError("Value can't be negative or zero")

    return a * a


def perimeter(a):
    '''
    Принимает на вход десятичное число a (int), возвращает периметр квадрата

    '''
    if a <= 0:
        raise ValueError("Value can't be negative or zero")

    return 4 * a
