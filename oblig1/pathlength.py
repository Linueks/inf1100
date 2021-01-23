from math import sqrt

x_coords = [1, 5, 2]
y_coords = [2, 6, 2]

def pathlength(x, y):
    """
    This function returns the length from
    x_coords[0], y_coords[0] to x_coords[n], y_coords[n]
    """

    length = 0
    for i in range (1, len(x)):
        length += sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2)
    return length

def test_pathlength():
    """
    This function tests the pathlength function on a precalculated problem
    The test problem is reflected in the values of x_coords and y_coords
    Functions returns True if the pathlength(x, y) is within 0.01 of the
    test problem.
    """

    expected_pl = 10.66
    error = expected_pl - pathlength(x_coords, y_coords)
    return error < 0.01



print pathlength(x_coords, y_coords)

print test_pathlength()
