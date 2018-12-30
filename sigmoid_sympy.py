from sympy import *
import numpy as np

z = symbols('z', float = True)
sigmoid = 1 / (1 + exp(-z))
pprint(sigmoid)
print()

values = np.arange(-5, 5.1, 0.1)
do_graph = True
s_vals = []

for i in values:
    val = N(sigmoid.subs(z, i))
    s_vals.append(val)
    print("{0:1.1f}".format(i), '\t', val)

sigmoid_prime = sigmoid.diff()
pprint(sigmoid_prime)
print()

sp_vals = []

for i in values:
    val = N(sigmoid_prime.subs(z, i))
    sp_vals.append(val)
    print("{0:1.1f}".format(i), '\t', val)

if do_graph:
    import matplotlib.pyplot as plt

    fig = plt.figure()
    axes = fig.add_subplot(111)

    x_vals = values

    axes.grid()
    axes.plot(x_vals, s_vals)

    plt.show();