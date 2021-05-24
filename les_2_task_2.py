# 2. Найти сумму и произведение матриц
# A=( 1 −2 ) и B =( 4 −1 )
#   ( 3  0 )      ( 0 -5 )
import numpy as np

a = np.array([[1, -2], [3, 0]])
b = np.array([[4, -1], [0, -5]])
print(f'Матрица С = A + B\n{a + b}')
print(f'Матрица С = A * B\n{np.dot(a, b)}')
