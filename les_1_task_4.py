# Найти координаты вектора 3x2−2x+2∈R3[x]:
# а) в базисе 1, x, x^2
# б) в базисе x^2, x−1, 1
import numpy as np


m1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = np.array([[1, 0, 0], [0, 1, -1], [0, 0, 1]])
vec = np.array([2, -2, 3])
# print(np.linalg.det(m1))
# print(np.linalg.det(m2))

# метод 1
print('a) 1. Коорднаты вектора в базисе 1, x, x^2: ', np.linalg.solve(m1, vec))
print('б) 1. Коорднаты вектора в базисе x^2, x−1, 1: ', np.linalg.solve(m2, vec))

# метод 2
reverse_m1 = np.linalg.inv(m1)
reverse_m2 = np.linalg.inv(m2)
print('a) 2. Коорднаты вектора в базисе 1, x, x^2: ', np.matmul(reverse_m1, vec))
print('б) 2. Коорднаты вектора в базисе x^2, x−1, 1: ', np.matmul(reverse_m2, vec))


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


print('a) 3. Коорднаты вектора в базисе 1, x, x^2: ', kramer(m1, vec))
print('б) 3. Коорднаты вектора в базисе x^2, x−1, 1: ', kramer(m2, vec))
