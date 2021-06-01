# 1. Решить систему уравнений методом Гаусса:
# ⎧ x1+x2−x3−2x4=0
# ⎨ 2x1+x2−x3+x4=−2
# ⎩ x1+x2−3x3+x4=4

import numpy as np

myA = np.array([[1, 1, -1, -2], [2, 1, -1, 1], [1, 1, -3, 1]])
myB = np.array([0, -2, 4])


def Output(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None or
                                                  selected != (row, col)) else "*", A[row][col]), end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))


# ---перемена местами двух строк системы
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


# ---деление строки системы на число
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


# ---сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight)
              for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


# ---решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(A, B):
    column = 0
    while column < len(B):
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
            if current_row is None:
                print("решений нет")
                return None
            Output(A, B, (current_row, column))

            if current_row != column:
                print("Переставляем строку с найденным элементом повыше:")
                SwapRows(A, B, current_row, column)
            Output(A, B, (column, column))

            print("Нормализуем строку с найденным элементом:")
            DivideRow(A, B, column, A[column][column])
            Output(A, B, (column, column))

            print("Обрабатываем нижележащие строки:")
            for r in range(column + 1, len(A)):
                CombineRows(A, B, r, column, -A[r][column])
            Output(A, B, (column, column))

            column += 1

    print("Матрица приведена к треугольному виду, считаем решение")
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("Получили ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(X)))

    return X


print("Исходная система уравнений:")
Output(myA, myB, None)
print("Решение СЛАУ:")
Gauss(myA, myB)
