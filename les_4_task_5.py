# 5. Решить систему уравнений методом Крамера:
# а)
# ⎧ x1−2x2=1
# ⎩ 3x1−4x2=7
# б)
# ⎧ 2x1−x2+5x3=10
# ⎨ x1+x2−3x3=−2
# ⎩ 2x1+4x2+x3=1

import numpy as np

print('а)')
a = np.array([[1, -2], [3, -4]])
x1 = np.array([1, 7])


def kramer(matrix, vector):
    m = len(matrix)
    op = np.linalg.det(matrix)
    r = list()
    for i in range(m):
        vm = np.copy(matrix)
        vm[:, i] = vector
        r.append(np.linalg.det(vm) / op)
    return r


print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(kramer(a, x1))))


print('б)')
b = np.array([[2, -1, 5], [1, 1, -3], [2, 4, 1]])
x2 = np.array([10, -2, 1])


def kramer(matrix, vector):
    m = len(matrix)
    op = np.linalg.det(matrix)
    r = list()
    for i in range(m):
        vm = np.copy(matrix)
        vm[:, i] = vector
        r.append(np.linalg.det(vm) / op)
    return r


print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(kramer(b, x2))))
