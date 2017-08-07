from typing import List
from math import fsum


class Domain:
    def __init__(self, x0: float, x1: float):
        assert x1 >= x0
        self.x0 = x0
        self.x1 = x1

    def __contains__(self, x: float):
        return self.x0 <= x and x <= self.x1

    def __str__(self):
        return "[{0.x0:.2f}, {0.x1:.2f}]".format(self)

    def len(self):
        return abs(self.x1 - self.x0)

    def __getitem__(self, index: int):
        return [self.x0, self.x1][index]

    def __iter__(self):
        yield self.x0
        yield self.x1

    def median(self):
        return fsum(self) / 2.


class Function:
    def __init__(self, **kwargs):
        self.f = kwargs.get('f', lambda: 0)
        self.domain = kwargs.get('domain')
        self.description = kwargs.get('description', '<func>')
        self.x0 = kwargs.get('x0')
        self.curve = kwargs.get('curve')

    def __call__(self, *args: List[float]):
        if self.domain:
            assert args[0] in self.domain
        return self.f(*args)

    def __str__(self):
        return self.description

    def __format__(self, fmt):
        return '{:{fmt}}'.format(str(self), fmt=fmt)

    def derivative(self, *args, **kwargs):
        """
        *args - point to calculate derivative at\n
        epsilon=1e-5 - tolerance\n
        index=0 - which argument to augment
        """
        epsilon = kwargs.get('epsilon', 1e-5)
        assert epsilon > 0
        index = kwargs.get('index', 0)
        augmented_args = list(args)
        augmented_args[index] += epsilon
        return (self.f(*augmented_args) - self.f(*args)) / epsilon

    def gradient(self, *args, **kwargs):
        """
        *args - point to calculate gradient at\n
        epsilon=1e-5 - tolerance
        """
        epsilon = kwargs.get('epsilon', 1e-5)
        return tuple(self.derivative(*args, index=i, epsilon=epsilon) for i in range(0, len(args)))
