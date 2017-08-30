from typing import Iterable
from math import fsum
from functools import reduce, partial
from itertools import repeat


def square(side):
    return side * side


def identity(value):
    return value


def const(return_value):
    return lambda *args: return_value


def negate(x):
    return -x


def flatten(iterable):
    for maybe_iterable in iterable:
        try:
            for value in maybe_iterable:
                yield value
        except TypeError:
            yield maybe_iterable


def is_number(value):
    return isinstance(value, int) or isinstance(value, float)


def close_to(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance


def fst(tpl):
    return tpl[0]


def snd(tpl):
    return tpl[1]


def swap(i, j, it):
    tmp = it[i]
    it[i] = it[j]
    it[j] = tmp
    return it


def product(*args):
    return reduce(lambda x, y: x * y, flatten(args), 1)


def hessian_matrix(func, args: Iterable[float], epsilon: float):
    args_range = range(func.get_argument_count())
    return [
        [func.derivative2(*args, epsilon=epsilon, index1=i, index2=j)
         for j in args_range]
        for i in args_range]


def append_column(matrix, column):
    return [list(row) + [column[i]] for i, row in enumerate(matrix)]


def jacobian_matrix(funcs, args, epsilon=1e-5):
    args_range = range(len(args))
    return [
        [func.derivative(*args, index=i, epsilon=epsilon)
         for i in args_range]
        for func in funcs]


def mxsum(*args: Iterable[Iterable[Iterable[float]]]):
    return reduce(partial(map, partial(map, fsum)), args, repeat(repeat(0)))
