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
