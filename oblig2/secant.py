from __future__ import division
from math import sin
import matplotlib.pyplot as plt
import numpy as np



def secant(f, xm2, xm1, n, epsilon = 1.0E-4):
    """
    The secant function takes x(n-2) = xm2 and x(n-1) = xm1, as well as n as arguments.
    When first passed to the function the x(n-2) = x0 and x(n-1) = x1, but i didn't like
    the names x0 and x1 as the variable names because it got confusing. (This function requires
    that your chosen x0 and x1 are 'close' the root)
    """

    root_approx = []

    for i in xrange(n):
        if abs(f(xm1)) <= epsilon:
            root_approx.append(xm1)
            return root_approx
        xn = xm1 - f(xm1) * (xm1 - xm2) / (f(xm1) - f(xm2))
        xm1, xm2 = xn, xm1
        root_approx.append(xm1)

    return root_approx

def f(x):
    return x ** 5 - np.sin(x)

#x = np.linspace(-2, 2, 100)
#plt.plot(x, f(x))
#plt.grid()
#plt.show()


if __name__ == '__main__':
    print secant(f, 1, 5, 20)

"""
[Linueks@1x-193-157-198-148 oblig2]$ python secant.py
0.961036943488
"""
