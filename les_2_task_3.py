# 3. Из закономерностей сложения и умножения матриц на число можно сделать вывод, что матрицы одного размера образуют
# линейное пространство. Вычислить линейную комбинацию 3A−2B+4C для матриц A=(1  3), B=(0  5), C=(2 −4).
#                                                                            (7 −6)    (2 −1)    (1  1)
import numpy as np

a = np.array([[1, 3], [7, -6]])
b = np.array([[0, 5], [2, -1]])
c = np.array([[2, -4], [1, 1]])
result = 3 * a - 2 * b + 4 * c
print(result)
