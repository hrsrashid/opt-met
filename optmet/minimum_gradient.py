from optmet.function import Function
from optmet.vector import Vector


def find_minimum_gradient(func: Function, epsilon=1e-5, delta=1e-2, **kwargs):
    current = Vector(*func.x0) or kwargs.get('x0') or Vector(0)
    step_size = abs(current)

    while step_size > epsilon:
        previous = Vector(*current)
        current += -delta * func.gradient(*previous, epsilon=epsilon)
        step_size = abs(current - previous)

    return current
