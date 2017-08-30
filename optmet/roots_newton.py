from typing import Iterable
from itertools import repeat
from optmet.function import Function
from optmet.vector import Vector
from optmet.lib import jacobian_matrix, append_column
from optmet.roots_gauss import roots_gauss


def roots_newton(funcs: Iterable[Function], epsilon=1e-5, **kwargs):
    assert epsilon > 0
    current = kwargs.get('x0', Vector(*repeat(0, len(funcs))))
    difference = epsilon + 1

    while difference > epsilon:
        previous = Vector(*current)
        f_current = Vector(
            *map(lambda func: func(*current), funcs))
        mx_jacobian = append_column(jacobian_matrix(
            funcs, current, epsilon=epsilon), -f_current)
        delta_x = roots_gauss(mx_jacobian, epsilon=epsilon)
        current += Vector(*delta_x)
        difference = abs(current - previous)

    return current
