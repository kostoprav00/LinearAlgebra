# 1.Найти с помощью NumPy SVD для матрицы
#  ⎛1  2 0⎞
#  ⎜0  0 5⎜
#  ⎜3 -4 2⎜
#  ⎜1  6 5⎜
#  ⎝0  1 0⎠

import numpy as np

A = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])

U, s, W = np.linalg.svd(A)
print('U:\n', U, '\n S:\n', s, '\n W:\n', W)

S = np.diag(s)
S = np.vstack([S, np.zeros((2, 3))])
print(np.allclose(A, np.dot(U, np.dot(S, W))))
