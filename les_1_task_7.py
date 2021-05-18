# Найти нормы векторов (4,2,4) и (12,3,4) и угол между ними.

import numpy as np
from numpy import linalg


x = [4, 2, 4]
y = [12, 3, 4]
print('Норма вектора (4,2,4): ', linalg.norm(x, ord=2))
print('Норма вектора (12,3,4): ', linalg.norm(y, ord=2))
print('Угол между векторами: ', np.dot(x, y) / linalg.norm(x) / linalg.norm(y))
