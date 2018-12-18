# функции которые используются в програме
import math
from math import sin

def add(a, b):
    """add - функция которая находит сумму двух чисел"""
    return a + b


def sub(a, b):
    """sub - функция которая находит разницу двух чисел"""
    return a - b


def mul(a, b):
    """mul-функция которая умножает одно число на другое"""
    return a * b

def div(a, b):
    """div-функция которая делит одно число на другое"""

    res = None
    try:
        res = a / b

    except(ZeroDivisionError) as e:
        print('!!! Error2:', e)
        print('Try again')
    return res

list_of_oper = {'+': add, '-': sub, '*': mul, '/': div}
