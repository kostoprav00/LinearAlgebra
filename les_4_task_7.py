# 7*. Решить систему линейных уравнений методом LU-разложения
# ⎧ 2x1+x2+3x3=1
# ⎨ 11x1+7x2+5x3=−6
# ⎩ 9x1+8x2+4x3=−5


import numpy as np
from scipy.linalg import lu

A = np.array([[2, 1, 3], [11, 7, 5], [9, 8, 4]])
B = np.array([1, -6, -5])


def decompose_to_LU(a):
    lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]
    for k in range(n):
        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]
        for i in range(k + 1, n):
            lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]
    return lu_matrix


def solve_lu(a, b):
    LU = decompose_to_LU(A)
    b = np.array(b, float)
    for i in range(1, len(b)):
        b[i] = b[i] - np.dot(LU[i, :i], b[:i])
    for i in range(len(b) - 1, -1, -1):
        b[i] = (b[i] - np.dot(LU[i, i + 1:], b[i + 1:])) / LU[i, i]
    return b


X = solve_lu(decompose_to_LU(A), B)
print('X1 = ', X[0])
print('X2 = ', X[1])
print('X3 = ', X[2])

