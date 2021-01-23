from math import sqrt, cos, sin, pi

def pathlength(x, y):
    """
    This function returns the length from
    x_coords[0], y_coords[0] to x_coords[n], y_coords[n]
    """

    length = 0
    for i in range (1, len(x)):
        length += sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2)
    return length

def pi_approx(n):
    """
    This function generates two lists x_val and y_val which are n points around a circle
    and returns a calculation of the pathlength of said points.
    """

    x_val = []
    y_val = []

    for i in range(0, n):
        x = 0.5 * cos(2 * pi * i / float(n))
        x_val.append(x)
        y = 0.5 * sin(2 * pi * i / float(n))
        y_val.append(y)

    return pathlength(x_val, y_val)

"""
This loop generates different n values to be fed into the pi_approx function
and prints the difference between pi and pi_approx for growing values of n
"""
for k in range(2, 10):
    n = 2 ** k
    approx = pi_approx(n)
    print pi - approx
