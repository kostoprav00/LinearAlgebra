# 5*. Написать на Python функцию для перемножения двух произвольных матриц, не используя NumPy.

import random


def summa():
    # Вводим размер матриц
    r1 = int(input('Количество элементов в строке матрицы 1: '))
    c1 = int(input('Количество элементов в столбце матрицы 1: '))
    r2 = int(input('Количество элементов в строке матрицы 2: '))
    c2 = int(input('Количество элементов в столбце матрицы 2: '))
    A = [[random.randrange(0, 10) for y in range(r1)] for x in range(c1)]
    B = [[random.randrange(0, 10) for y in range(r2)] for x in range(c2)]

    # Умножение
    s = 0  # сумма
    t = []  # временная матрица
    C = []  # конечная матрица
    if len(B) != len(A[0]):
        print('Матрицы не могут быть перемножены')
    else:
        r1 = len(A)  # количество строк в первой матрице
        c1 = len(A[0])  # Количество столбцов в 1
        r2 = c1  # и строк во 2ой матрице
        c2 = len(B[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + A[z][i] * B[i][j]
                t.append(s)
                s = 0
            C.append(t)
            t = []
    return C


print(summa())
