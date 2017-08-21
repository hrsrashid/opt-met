from array import array
from optmet.lib import flatten, is_number, close_to


class Vector:
    def __init__(self, *args):
        self.components = array('d', flatten(args))

    def __getitem__(self, index: int):
        return self.components[index]

    def __str__(self, **kwargs):
        predicate = kwargs.get('predicate', str)
        return '(' + ', '.join(map(predicate, self.components)) + ')'

    def __repr__(self):
        return self.__str__()

    def __format__(self, fmt):
        return self.__str__(predicate=lambda x: '{:{fmt}}'.format(x, fmt=fmt))

    def __abs__(self):
        return max(map(abs, self.components))

    def __bool__(self):
        return len(self.components) > 0

    def __eq__(self, operand):
        if isinstance(operand, Vector):
            return all(map(close_to, self, operand))
        if is_number(operand):
            return len(self.components) == 1 and close_to(self[0], operand)

    def __neg__(self):
        return Vector(-x for x in self.components)

    def __mul__(self, operand):
        if isinstance(operand, Vector):
            raise NotImplementedError()
        if is_number(operand):
            return Vector(operand * x for x in self.components)

    def __rmul__(self, operand):
        return self * operand

    def __truediv__(self, operand):
        if isinstance(operand, Vector):
            raise NotImplementedError()
        if is_number(operand):
            return self * (1 / operand)

    def __add__(self, operand):
        if isinstance(operand, Vector):
            return Vector(map(lambda l, r: l + r, self.components, operand))
        if is_number(operand):
            return Vector(x + operand for x in self.components)

    def __radd__(self, operand):
        return self + operand

    def __sub__(self, operand):
        return self + -operand

    def __rsub__(self, operand):
        return operand + -self

    def __iadd__(self, operand):
        self.components = (self + operand).components
        return self
