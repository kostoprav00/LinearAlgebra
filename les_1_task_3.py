# Найти координаты вектора x=(2,3,5)∈R3 в базисе b1=(0,0,10), b2=(2,0,0), b3=(0,1,0).

import numpy as np

# метод 1
b = np.array([[0, 0, 10], [2, 0, 0], [0, 1, 0]])
x = np.array([2, 3, 5])
print('1) Новые коорднаты вектора x: ', np.linalg.solve(b, x))

# метод 2
reverse_b = np.linalg.inv(b)
print('2) Новые коорднаты вектора x: ', np.matmul(reverse_b, x))


# метод 3
def kramer(matrix, vector):
    m = len(matrix)
    op = np.linalg.det(matrix)
    r = list()
    for i in range(m):
        vm = np.copy(matrix)
        vm[:, i] = vector
        r.append(np.linalg.det(vm) / op)
    return r


print('3) Новые коорднаты вектора x: ', kramer(b, x))
