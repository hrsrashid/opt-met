#!/usr/bin/env python3

import optmet.tasks as tasks
from optmet.minimum_gradient import find_minimum_gradient

for task_num in tasks.TASKS['4']:
    function = tasks.FUNCTIONS[task_num]
    minimum = find_minimum_gradient(function, tasks.EPSILON)
    print("minimum of {0} is {1:.2f}".format(
        function, minimum), flush=True)
