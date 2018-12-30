from sympy import *

x, y, z = symbols('x y z')
exp = x**4 + 4 * x ** 3 + 3 * x ** 2
print('f(x) = ', exp)
print('f(10) = ', exp.subs(x, 10))
print("f\'(x) = ", exp.diff())
print("f\'(10) = ", exp.diff().subs(x, 10))
integral = Integral(sqrt(1/x), x)
print("Pretty printing integral: ")
pprint(integral)
