from sympy import *
import numpy as np
#import matplotlib.pyplot as plt

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
    #print("{0:1.1f}".format(i), '\t', val)

sigmoid_prime = sigmoid.diff()
pprint(sigmoid_prime)
print()
sigmoid_prime_simpl = sigmoid_prime * exp(2 * z) / exp(2 * z)
pprint(sigmoid_prime_simpl)


sp_vals = []

for i in values:
    val = N(sigmoid_prime.subs(z, i))
    sp_vals.append(val)
    print("{0:1.1f}".format(i), '\t', val)

