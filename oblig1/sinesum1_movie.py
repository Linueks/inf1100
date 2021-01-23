"""Program plots the evolution of S(t;n) as n increases
compared to the static function it is meant to approximate.
Using FuncAnimation."""

import matplotlib.pyplot as plt
import sinesum2
from matplotlib import animation
from math import pi
from numpy import linspace, zeros

def f(t, T):
    """See sinesum2.py"""
    return sinesum2.f(t, T)

def S(t, n, T):
    """See sinesum2.py"""
    return sinesum2.S(t, n, T)

T = 2 * pi
t = linspace(0, T, 201)

y = zeros(len(t))

for i in xrange(0, 200):
    y[i] = f(t[i], T)

fig = plt.figure()
plt.axis([t[0], t[-1], -2, 2])
actual_plot = plt.plot([], [])
approx_plot = plt.plot([], [])
plt.xlabel('t')
plt.ylabel('y')

def init():
    actual_plot[0].set_data(t, y)
    approx_plot[0].set_data(t, y)
    return approx_plot

def frame(n):
    y = zeros(len(t))
    for i in range(len(t)):
        y[i] = S(t[i], n, T)
    approx_plot[0].set_data(t, y)
    return approx_plot

frames = range(0, 200)

anim = animation.FuncAnimation(
    fig, frame, frames, interval = 200, init_func = init, blit = True
)

plt.show()
