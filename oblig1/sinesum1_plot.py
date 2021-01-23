"""Program for plotting different values for S(t;n) over the plot for f(t)"""

import sinesum2
import matplotlib.pyplot as plt
from numpy import linspace, zeros
from math import pi

def f(t, T):
    """See sinesum2.py"""
    return sinesum2.f(t, T)

def S(t, n, T):
    """See sinesum2.py"""
    return sinesum2.S(t, n, T)

def calc(n):
    """Calculates y values for the approximation function"""
    y = zeros(len(t))
    for i in xrange(len(t)):
        y[i] = S(t[i], n, T)

    return y

T = 2 * pi

t = linspace(0, T, 120)
actual_y = zeros(len(t))
for i in xrange(len(t)):
    actual_y[i] = f(t[i], T)

n_vals = [1, 3, 20, 200]
plt.hold('on')

legends = []

"""Loop to plot different S(t;n) curves + make a legend listing n and function"""
for n in n_vals:
    y = calc(n)
    plt.plot(t, y)
    legends.append("S(t; " + repr(n) + ")")

"""Plotting exact plot last to get line on top to enhance visibility"""
plt.plot(t, actual_y, 'k-')

legends.append("f(x)")

plt.legend(tuple(legends))

plt.xlabel('Values of t')
plt.ylabel('Values of y')
plt.show()
