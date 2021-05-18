# Исследовать на линейную зависимость:
# f1(x)=2,f2(x)=x,f3(x)=x^2,f4(x)=(x+1)^2
# f4(x) = x^2 + 2x + 1 = f3(x) + f1(x)*f2(x) + f1(x)/2

from sympy import *

x = Symbol('x')
expr1 = x * 0 + 2
expr2 = x
expr3 = x ** 2
expr4 = (x + 1) ** 2

vronskiy = Matrix(
    [
        [expr1, expr2, expr3, expr4],
        [expr1.diff(x), expr2.diff(x), expr3.diff(x), expr4.diff(x)],
        [expr1.diff(x).diff(x), expr2.diff(x).diff(x), expr3.diff(x).diff(x), expr4.diff(x).diff(x)],
        [expr1.diff(x).diff(x).diff(x), expr2.diff(x).diff(x).diff(x), expr3.diff(x).diff(x).diff(x),
         expr4.diff(x).diff(x).diff(x)]
    ])

if vronskiy.det() == 0:
    print('Комбинация векторов линейно зависима')
else:
    print('Комбинация векторов линейно независима')
