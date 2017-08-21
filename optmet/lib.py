def square(side):
    return side * side


def identity(value):
    return value


def const(return_value):
    return lambda *args: return_value


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
    n_args = func.get_argument_count()
    return [
        [func.derivative2(*args, epsilon=epsilon, index1=i, index2=j)
         for j in range(0, n_args)]
        for i in range(0, n_args)]


def roots_gauss(matrix, epsilon=1e-5):
    m = len(matrix)
    n = len(matrix[0])

    for k in range(min(m, n)):
        i_max, _ = max(((i, abs(matrix[i][k])) for i in range(k, m)), key=snd)

        if close_to(matrix[i_max][k], 0, tolerance=epsilon):
            raise Exception("Matrix is singular!")

        swap(k, i_max, matrix)

        for i in range(k + 1, m):
            coefficient = matrix[i][k] / matrix[k][k]
            for j in range(k + 1, n):
                matrix[i][j] = matrix[i][j] - matrix[k][j] * coefficient

            matrix[i][k] = 0

    roots = deque()
    for i in range(m - 1, -1, -1):
        row = list(filter(None, matrix[i]))
        roots.appendleft(
            (row[-1] - fsum(map(product, zip(row[1:-1], roots)))) / row[0])

    return list(roots)


def append_column(matrix, column):
    return [list(row) + [column[i]] for i, row in enumerate(matrix)]
