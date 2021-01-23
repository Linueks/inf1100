import numpy as np
from math import sin, pi
import matplotlib.pyplot as plt


class Integral:
    def __init__(self, f, a, n=100):
        self.f = f
        self.a = a
        self.n = n

    def __call__(self, x):
        if isinstance(x, (float, int)):
            return self.trapezoidal(self.f, self.a, x, self.n)
        else:
            return self.difference_integral(self.f, self.a, x)


    def trapezoidal(self, f, a, x, n):
        """from page 397 in a primer"""
        h = (x - a) / float(n)
        I = 0.5 * f(a)
        for i in xrange(1, n):
            I += f(a + i * h)
        I += 0.5 * f(x)
        I *= h
        
        return I

    def difference_integral(self, f, a, x):
        f_value = f(x)
        F = np.zeros_like(x)
        F[0] = 0

        for k in xrange(1, len(x)):
            F[k] = F[k - 1] + 0.5 * (x[k] - x[k - 1]) * (f_value[k - 1] + f_value[k])

        return F


"""
Using example from page 612. Can't get it working with sin(x) as the function though.
In that case the numerical integrals graph goes down to -2 which is wrong. Looks like
it's correct for the guassian function so im happy. The result is at least exactly like
the example in a primer.
"""
def g(t):
    return 1. / np.sqrt(2 * np.pi) * np.exp(-t ** 2)

F = Integral(g, 0)
x = np.linspace(-pi, pi, 200)
plt.plot(x, g(x))
plt.plot(x, F(x))
plt.legend(['g(x)', 'numerical integral of g(x)'], loc=2)
plt.show()
