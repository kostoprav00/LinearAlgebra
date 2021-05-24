# 9.  Найти ранг матрицы:
# а)
# (1 2 3)
# (1 1 1)
# (2 3 4)
# б)
# (0 0 2 1)
# (0 0 2 2)
# (0 0 4 3)
# (2 3 5 6).
import numpy as np

print('a)')
x = [1, 2, 3]
y = [1, 1, 1]
z = [2, 3, 4]

a = np.array([x, y, z])
r = np.linalg.matrix_rank(a)

print(f'Ранг матрицы: {r}')

print('б)')
x1 = [0, 0, 2, 1]
y1 = [0, 0, 2, 2]
z1 = [0, 0, 4, 3]
d1 = [0, 0, 4, 3]

a1 = np.array([x1, y1, z1, d1])
r1 = np.linalg.matrix_rank(a1)
print(f'Ранг матрицы: {r1}')
