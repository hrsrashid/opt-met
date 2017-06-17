#!/usr/bin/env python3

import tasks
from minimum_fibo import find_minimum_fibo

for task_num in tasks.TASKS['2']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_fibo(function, tasks.EPSILON)
    print("minimum of {0:^15} is {1: 5.2f} in {0.domain}".format(
        function, minimum), flush=True)
