# 6. Вычислить определитель:
# a)
# ∣sinx −cosx∣
# ∣cosx  sinx∣;
# б)
# ∣4 2 3∣
# ∣0 5 1∣
# ∣0 0 9∣;
# в)
# ∣1 2 3∣
# ∣4 5 6∣
# ∣7 8 9∣.
import numpy as np
import math

print('a)')
x = 0
c = np.array([[math.sin(x), -math.cos(x)], [math.cos(x), math.sin(x)]])
print(f'Определитель:{np.linalg.det(c):.0f}')
print('б)')
a = np.array([[4, 2, 3], [0, 5, 1], [0, 0, 9]])
print(f'Определитель:{np.linalg.det(a):.0f}')
print('в)')
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Определитель:{np.linalg.det(b):.0f}')
