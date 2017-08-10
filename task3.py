#!/usr/bin/env python3

import optmet.tasks as tasks
from optmet.minimum_hessian import find_minimum_hessian

for task_num in tasks.TASKS['3']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_hessian(function, tasks.EPSILON)
    print("minimum of {0:^15} is {1: 5.2f}".format(
        function, minimum), flush=True)
