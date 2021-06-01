# 6.Найти L-матрицу LU-разложения для матрицы коэффициентов:
# а)
#  ⎛1  2  4⎞
#  ⎜2  9 12⎜
#  ⎝3 26 30⎠
# б)
#  ⎛1  1  2  4⎞
#  ⎜2  5  8  9⎜
#  ⎜3 18 29 18⎜
#  ⎝4 22 53 33⎠
import numpy as np

A = np.array([[1, 2, 4], [2, 9, 12], [3, 26, 30]])
B = np.array([[1, 1, 2, 4], [2, 5, 8, 9], [3, 18, 29, 18], [4, 22, 53, 33]])


def decompose_to_LU(a):
    lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]

    for k in range(n):

        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]

        for i in range(k + 1, n):
            lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]

    return lu_matrix


def get_L(m):
    L = m.copy()
    for i in range(L.shape[0]):
        L[i, i] = 1
        L[i, i + 1:] = 0
    return np.matrix(L)


print('а)', get_L(decompose_to_LU(A)))
print('б)', get_L(decompose_to_LU(B)))
