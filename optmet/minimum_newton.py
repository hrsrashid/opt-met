from optmet.function import Function
from optmet.vector import Vector
from optmet.lib import roots_gauss, hessian_matrix, append_column


def find_minimum_newton(func: Function, epsilon=1e-5, **kwargs):
    current = func.x0 or kwargs.get('x0', Vector(0))
    difference = abs(current)

    while difference > epsilon:
        previous = Vector(*current)
        mx_hessian = append_column(hessian_matrix(
            func, current, epsilon=epsilon), -func.gradient(*current))
        delta_x = roots_gauss(mx_hessian, epsilon=epsilon)
        current += Vector(*delta_x)
        difference = abs(current - previous)

    return current
