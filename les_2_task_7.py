# 7. Определитель матрицы A равен 4. Найти:
# а) det(A^2);
# б) det(A^T);
# в) det(2A).
import numpy as np

# в) det(2A).
print('det(2A) = 2*4 = 8')

a = np.array([[4, 0, 0], [0, 1, 0], [0, 0, 1]])
print(a)
c = np.dot(a, a)
print('а) det(A^2) = det(A)·det(A) = 16')
print(f"det(A^2) ={round(np.linalg.det(c))}")
print(f"det(A)·det(A) ={np.linalg.det(a) * np.linalg.det(a)}")
print("#########################################")
print('б) det(A^T) = 4')
print(f"det(A^T) = {np.linalg.det(a.T)}")
print("#########################################")
print('в) det(2A) = 2*4 = 8')
print(f"det(2A) = {2 * np.linalg.det(a)}")
