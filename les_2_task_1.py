# Все задания рекомендуется делать вручную, затем проверяя полученные результаты с использованием numpy.
# 1. Установить, какие произведения матриц AB и BA определены, и найти размерности полученных матриц:
# а) A — матрица 4×2, B — матрица 4×2;
# б) A — матрица 2×5, B — матрица 5×3;
# в) A — матрица 8×3, B — матрица 3×8;
# г) A — квадратная матрица 4×4, B — квадратная матрица 4×4.

import random


def generate_matrix( col_size, row_size ):
    return [[random.randrange(0, 10) for y in range(row_size)] for x in range(col_size)]


def is_determined( first_matrix, second_matrix ):
    if len(first_matrix[0]) == len(second_matrix):
        return True
    return False


def analyze_multiplexing_of_matrix( a, b ):
    print(f"A is {a}")
    print(f"B is {b}")
    if is_determined(a, b):
        print("AxB is determined. Calculating C=AxB....")
        row_count = len(a)
        col_count = len(b[0])
        print(f"C has {row_count} rows & {col_count} columns")
    else:
        print("AxB is undefined")


A = generate_matrix(4, 2)
B = generate_matrix(4, 2)
analyze_multiplexing_of_matrix(A, B)
analyze_multiplexing_of_matrix(B, A)
print("#########################################")
A = generate_matrix(2, 5)
B = generate_matrix(5, 3)
analyze_multiplexing_of_matrix(A, B)
analyze_multiplexing_of_matrix(B, A)
print("#########################################")
A = generate_matrix(8, 3)
B = generate_matrix(3, 8)
analyze_multiplexing_of_matrix(A, B)
analyze_multiplexing_of_matrix(B, A)
print("#########################################")
A = generate_matrix(4, 4)
B = generate_matrix(4, 4)
analyze_multiplexing_of_matrix(A, B)
analyze_multiplexing_of_matrix(B, A)
