from typing import Iterable
from optmet.function import Function


def find_minimum_hessian(func: Function, epsilon: float):
    return 0


def hessian_matrix(func: Function, args: Iterable[float], epsilon: float):
    n_args = func.get_argument_count()
    return [
        [func.derivative2(*args, epsilon=epsilon, index1=i, index2=j)
         for j in range(0, n_args)]
        for i in range(0, n_args)]
