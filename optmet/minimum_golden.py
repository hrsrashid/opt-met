from math import sqrt
from optmet.function import Function, Domain


GOLDEN_RATIO = (sqrt(5) + 1) / 2


def find_minimum_golden(func: Function, epsilon: float) -> float:
    assert func.domain

    span = Domain(*func.domain)
    r = right(span)
    l = left(span)

    while abs(r - l) > epsilon:
        if func(r) < func(l):
            span.x1 = l
        else:
            span.x0 = r

        r = right(span)
        l = left(span)

    return span.median()


def right(span: Domain):
    return span.x1 - span.len() / GOLDEN_RATIO


def left(span: Domain):
    return span.x0 + span.len() / GOLDEN_RATIO
