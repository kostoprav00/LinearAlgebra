# Какие из нижеперечисленных векторов образуют ортонормированный базис в линейном пространстве R3:
# а) (1,0,0),(0,0,1);
# б) (1/2–√,−1/2–√,0),(1/2–√,1/2–√,0),(0,0,1);
# в) (1/2,−1/2,0),(0,1/2,1/2),(0,0,1);
# г) (1,0,0),(0,1,0),(0,0,1)?
# Два ненулевых вектора x и y из En называются ортогональными, если скалярное произведение (x,y)=0
# Базис называется ортонормированным, если он ортогональный, а все его векторы имеют длину, равную единице.

import numpy as np
from math import *
print('а) ')
x1 = np.array([1, 0, 0])
y1 = np.array([0, 0, 1])
print('Данные вектора не являются ортонормированным базисом в линейном пространстве R3')


print('б) ')
x = np.array([1/sqrt(2), -1/sqrt(2), 0])
y = np.array([1/sqrt(2), 1/sqrt(2), 0])
z = np.array([0, 0, 1])
print(f'Длина вектора x: {round(np.linalg.norm(x))}')
print(f'Длина вектора y: {round(np.linalg.norm(y))}')
print(f'Длина вектора z: {np.linalg.norm(z)}')
print(f'Скалярное произведение x и y: {np.dot(x, y)}')
print(f'Скалярное произведение x и y: {np.dot(x, z)}')
print(f'Скалярное произведение x и y: {np.dot(y, z)}')
if round(np.linalg.norm(x)) == 1 and round(np.linalg.norm(y)) == 1 and np.linalg.norm(z) == 1 \
        and np.dot(x, y) == 0 and np.dot(x, z) == 0 and np.dot(y, z) == 0:
    print('Данные вектора образуют ортонормированный базис в линейном пространстве R3')
else:
    print('Данные вектора не являются ортонормированным базисом в линейном пространстве R3')


print('в) ')
x2 = np.array([1/2, -1/2, 0])
y2 = np.array([0, 1/2, 1/2])
z2 = np.array([0, 0, 1])
print(f'Длина вектора x: {np.linalg.norm(x2)}')
print(f'Длина вектора y: {np.linalg.norm(y2)}')
print(f'Длина вектора z: {np.linalg.norm(z2)}')
print(f'Скалярное произведение x и y: {np.dot(x2, y2)}')
print(f'Скалярное произведение x и y: {np.dot(x2, z2)}')
print(f'Скалярное произведение x и y: {np.dot(y2, z2)}')
if np.linalg.norm(x2) == 1 and np.linalg.norm(y2) == 1 and np.linalg.norm(z2) == 1 \
        and np.dot(x2, y2) == 0 and np.dot(x2, z2) == 0 and np.dot(y2, z2) == 0:
    print('Данные вектора образуют ортонормированный базис в линейном пространстве R3')
else:
    print('Данные вектора не являются ортонормированным базисом в линейном пространстве R3')


print('г) ')
x3 = np.array([1, 0, 0])
y3 = np.array([0, 1, 0])
z3 = np.array([0, 0, 1])
print(f'Длина вектора x: {np.linalg.norm(x3)}')
print(f'Длина вектора y: {np.linalg.norm(y3)}')
print(f'Длина вектора z: {np.linalg.norm(z3)}')
print(f'Скалярное произведение x и y: {np.dot(x3, y3)}')
print(f'Скалярное произведение x и y: {np.dot(x3, z3)}')
print(f'Скалярное произведение x и y: {np.dot(y3, z3)}')
if np.linalg.norm(x3) == 1 and np.linalg.norm(y3) == 1 and np.linalg.norm(z3) == 1 \
        and np.dot(x3, y3) == 0 and np.dot(x3, z3) == 0 and np.dot(y3, z3) == 0:
    print('Данные вектора образуют ортонормированный базис в линейном пространстве R3')
else:
    print('Данные вектора не являются ортонормированным базисом в линейном пространстве R3')



