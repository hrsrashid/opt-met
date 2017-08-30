from math import fsum
from optmet.vector import Vector
from optmet.function import Function
from optmet.roots_newton import roots_newton


def find_minimum_lagrange(func: Function, epsilon=1e-5, **kwargs):
    assert epsilon > 0
    constraint = func.constraint or kwargs.get('constraint')

    lagrangian = Function(
        f=lambda l, *args: func(*args) + l * constraint(*args))

    square_sum_grad_lagrangian = Function(f=lambda *args: fsum(lagrangian.derivative(
        *args, index=i, epsilon=epsilon)**2 for i, _ in enumerate(args)))

    f_system = list(map(lambda i:
                        Function(
                            f=lambda *args: square_sum_grad_lagrangian.derivative(
                                *args, index=i, epsilon=epsilon)),
                        range(func.get_argument_count() + 1)
                        ))

    return Vector(*roots_newton(f_system, epsilon)[1:])
