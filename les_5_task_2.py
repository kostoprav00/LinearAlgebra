# 2.Для матрицы найти:
#  ⎛1  2 0⎞
#  ⎜0  0 5⎜
#  ⎜3 -4 2⎜
#  ⎜1  6 5⎜
#  ⎝0  1 0⎠
#  а) евклидову норму;
# б) норму Фробениуса.
import numpy as np
from numpy import linalg as LA

L = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])
N = LA.linalg.norm(L, ord=2)
print('Евклидова норма: ', N)

N = LA.linalg.norm(L, ord='fro')
print('Норма Фробениуса: ', N)
