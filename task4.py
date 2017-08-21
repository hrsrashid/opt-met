#!/usr/bin/env python3

import optmet.tasks as tasks
from optmet.minimum_gradient import find_minimum_gradient
from optmet.minimum_newton import find_minimum_newton
from optmet.minimum_fletcher_reeves import find_minimum_fletcher_reeves


def pretty_print(prefix, function, minimum):
    print("{prefix:<20} minimum of {0} is {1:.2f}".format(
        function, minimum, prefix=prefix), flush=True)


for task_num in tasks.TASKS['4']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_gradient(function, tasks.EPSILON)
    pretty_print('gradient descent', function, minimum)
    minimum = find_minimum_newton(function, tasks.EPSILON)
    pretty_print('Newton`s method', function, minimum)
    minimum = find_minimum_fletcher_reeves(function, tasks.EPSILON)
    pretty_print('Fletcher-Reeves', function, minimum)
