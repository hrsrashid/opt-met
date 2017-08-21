from itertools import repeat
from optmet.function import Function, Domain
from optmet.vector import Vector
from optmet.minimum_golden import find_minimum_golden


def find_minimum_fletcher_reeves(func: Function, epsilon=1e-5, linear_minimizer=find_minimum_golden, **kwargs):
    current = func.x0 or kwargs.get('x0') or Vector(0)
    grad = func.gradient(*current)
    prev_grad_square = grad * grad
    step = 0
    space_size = func.get_argument_count()
    conjugate_dir = Vector(repeat(0, space_size))

    while abs(grad) > epsilon:
        grad_square = grad * grad
        if step % space_size == 0:
            alpha = 0
        else:
            alpha = grad_square / prev_grad_square
        prev_grad_square = grad_square

        conjugate_dir = grad + alpha * conjugate_dir
        phi = linear_minimizer(Function(f=lambda x: func(
            *(current - x * conjugate_dir)), domain=Domain(-1, 1)), epsilon=epsilon)
        displacement = phi * conjugate_dir

        current += displacement
        grad = func.gradient(*current)
        step += 1

    return current
