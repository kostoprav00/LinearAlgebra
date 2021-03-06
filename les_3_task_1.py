# 1. Найти собственные векторы и собственные значения для линейного оператора, заданного матрицей
# A = (−1 −6)
#     (2   6)
import numpy as np

a = np.array([[-1, -6], [2, 6]])
w, v = np.linalg.eig(a)

print(f'Матрица A:\n{a}')
print(f'Собственные значения:\n{w}')
print(f'Собственные векторы:\n{v}')
