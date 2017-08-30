from math import fsum
from collections import deque
from optmet.lib import swap, close_to, snd, product


def roots_gauss(matrix, epsilon=1e-5):
    m = len(matrix)
    n = len(matrix[0])

    for k in range(min(m, n)):
        i_max, _ = max(((i, abs(matrix[i][k])) for i in range(k, m)), key=snd)

        if close_to(matrix[i_max][k], 0, tolerance=epsilon):
            raise Exception("Matrix is singular!")

        swap(k, i_max, matrix)

        for i in range(k + 1, m):
            coefficient = matrix[i][k] / matrix[k][k]
            for j in range(k + 1, n):
                matrix[i][j] = matrix[i][j] - matrix[k][j] * coefficient

            matrix[i][k] = 0

    roots = deque()
    for i in range(m - 1, -1, -1):
        row = list(filter(None, matrix[i]))
        roots.appendleft(
            (row[-1] - fsum(map(product, zip(row[1:-1], roots)))) / row[0])

    return list(roots)
