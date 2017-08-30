#!/usr/bin/env python3

import optmet.tasks as tasks
from optmet.minimum_lagrange import find_minimum_lagrange

for task_num in tasks.TASKS['5']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_lagrange(function, tasks.EPSILON)
    print("minimum of {0:^37} is {1:.3f}".format(
        function, minimum), flush=True)
