from typing import Iterator
from itertools import takewhile
from function import Function, Domain


def find_minimum_fibo(func: Function, epsilon: float) -> float:
    assert func.domain

    f_seq = fiboUntil(func.domain.len() / epsilon)
    span = Domain(*func.domain)
    k = len(f_seq) - 1

    while k > 2:
        d = f_seq[k - 2] / f_seq[k] * span.len()

        if func(span.x0 + d) >= func(span.x1 - d):
            span.x0 += d
        else:
            span.x1 -= d

        k -= 1

    return span.median()


def fiboUntil(number) -> [int]:
    return list(takewhile(lambda x: x <= number, fibo_seq()))


def fibo_seq() -> Iterator[int]:
    yield 1

    p_1 = 1
    p_2 = 0

    while True:
        current = p_1 + p_2
        p_2 = p_1
        p_1 = current
        yield current
