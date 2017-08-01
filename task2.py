#!/usr/bin/env python3

import tasks
from minimum_fibo import find_minimum_fibo
from minimum_golden import find_minimum_golden


def pretty_print(prefix, function, minimum):
    print("{prefix}: minimum of {0:^15} is {1: 5.2f} in {0.domain}".format(
        function, minimum, prefix=prefix), flush=True)


for task_num in tasks.TASKS['2']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_fibo(function, tasks.EPSILON)
    pretty_print('fibo', function, minimum)
    minimum = find_minimum_golden(function, tasks.EPSILON)
    pretty_print('gold', function, minimum)
