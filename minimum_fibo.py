from typing import Iterator
from itertools import takewhile
from function import Function


def find_minimum_fibo(func: Function, epsilon: float) -> float:
    assert func.domain

    f_seq = fiboUntil(func.domain.len() / epsilon)
    a = func.domain.x0
    b = func.domain.x1
    k = len(f_seq) - 1

    while k > 2:
        d = f_seq[k - 2] / f_seq[k] * (b - a)

        if func(a + d) >= func(b - d):
            a += d
        else:
            b -= d

        k -= 1

    return (a + b) / 2


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
