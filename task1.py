#!/usr/bin/env python3

import optmet.tasks as tasks
from optmet.minimum_dichotomy import find_minimum_dichotomy

for task_num in tasks.TASKS['1']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_dichotomy(function, tasks.EPSILON, tasks.DELTA)
    print("minimum of {0:^15} is {1: 5.2f} in {0.domain}".format(
        function, minimum), flush=True)
