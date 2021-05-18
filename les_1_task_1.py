# Исследовать на линейную зависимость:
# f1(x)=e^x,f2(x)=1,f3(x)=x+1,f4(x)=x−e^x
# f4(x) = f3(x) - f2(x) - f1(x)

from sympy import *


x = Symbol('x')
expr4 = exp(x)
expr5 = x * 0 + 1
expr6 = x + 1
expr7 = x - exp(x)

vronskiy = Matrix(
    [
        [expr4, expr5, expr6, expr7],
        [expr4.diff(x), expr5.diff(x), expr6.diff(x), expr7.diff(x)],
        [expr4.diff(x).diff(x), expr5.diff(x).diff(x), expr6.diff(x).diff(x), expr7.diff(x).diff(x)],
        [expr4.diff(x).diff(x).diff(x), expr5.diff(x).diff(x).diff(x), expr6.diff(x).diff(x).diff(x),
         expr7.diff(x).diff(x).diff(x)]
    ])

if vronskiy.det() == 0:
    print('Комбинация векторов линейно зависима')
else:
    print('Комбинация векторов линейно независима')

