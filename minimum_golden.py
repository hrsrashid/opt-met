from math import sqrt
from function import Function, Domain


GOLDEN_RATIO = (sqrt(5) + 1) / 2


def find_minimum_golden(func: Function, epsilon: float) -> float:
    a, b = func.domain
    c = right(a, b)
    d = left(a, b)

    while abs(c - d) > epsilon:
        if func(c) < func(d):
            b = d
        else:
            a = c

        c = right(a, b)
        d = left(a, b)

    return (b + a) / 2


def right(a, b):
    return b - (b - a) / GOLDEN_RATIO


def left(a, b):
    return a + (b - a) / GOLDEN_RATIO
