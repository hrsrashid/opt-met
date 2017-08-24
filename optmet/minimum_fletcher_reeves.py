from optmet.function import Function, Domain
from optmet.vector import Vector
from optmet.minimum_golden import find_minimum_golden


def find_minimum_fletcher_reeves(func: Function, epsilon=1e-5, linear_minimizer=find_minimum_golden, **kwargs):
    current = Vector(*func.x0) or kwargs.get('x0') or Vector(0)
    difference = 0
    grad = func.gradient(*current, epsilon=epsilon)
    prev_grad_square = 1
    search_dir = 0

    while abs(grad) > epsilon:
        previous = Vector(*current)
        grad_square = grad * grad
        if difference < epsilon ** 2:
            alpha = 0
        else:
            alpha = grad_square / prev_grad_square
        prev_grad_square = grad_square

        search_dir = -grad + alpha * search_dir

        phi = linear_minimizer(Function(f=lambda x: func(
            *(current + x * search_dir)), domain=Domain(-100, 100)), epsilon=epsilon)

        current += phi * search_dir
        grad = func.gradient(*current, epsilon=epsilon)
        difference = abs(current - previous)

    return current
