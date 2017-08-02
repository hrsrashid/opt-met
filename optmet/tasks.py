from optmet.function import Function, Domain

EPSILON = .5
DELTA = .2

FUNCTIONS = {
    '25.1': Function(f=lambda x: x**2 + 5 * x - 1, domain=Domain(-3, 7), description='x² + 5x - 1'),
    '25.2': Function(f=lambda x: (x - 7)**2 - 3,   domain=Domain(-3, 7), description='(x - 7)² - 3'),
    '26.1': Function(f=lambda x: x**2 - 5 * x + 2, domain=Domain(-2, 8), description='x² - 5x + 2'),
    '26.2': Function(f=lambda x: (x + 7)**2 - 3,   domain=Domain(-2, 8), description='(x + 7)² - 3'),
    '15': Function(f=lambda x, y: x**2 + 6 * y**2 + x * y + x, x0=(1.5, 1.1), description='f = x² + 6y² + xy + x; x₀ = (1.5, 1.1)'),
    '25_2.1': Function(f=lambda x, y: 2 * x**2 + 5 * y**2 + x * y + x, curve=lambda x, y: x + .5 * y == 5, description='f = 2x² + 5y² + xy + x; x + 0.5y = 5'),
    '25_2.2': Function(f=lambda x, y: x**2 + 8 * y**2 + x * y + x, curve=lambda x, y: 3 * x + y == 2, description='f = x² + 8y² + xy + x; 3x + y = 2')
}

TASKS = {
    '1': ['25.1', '25.2', '26.1', '26.2'],
    '2': ['25.1', '25.2'],
    '3': ['15'],
    '4': ['15'],
    '5': ['25_2.1', '25_2.2']
}
