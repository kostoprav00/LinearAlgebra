#                   (4  1)
# 4. Дана матрица A=(5 -2). Вычислить A*A^T и A^T*A.
#                   (2  3)
import numpy as np

a = np.array([[4, 1], [5, -2], [2, 3]])
a_trans = a.T
print(f'A*A^T:\n{np.dot(a, a_trans)}')
print(f'A^T*A:\n{np.dot(a_trans, a)}')
