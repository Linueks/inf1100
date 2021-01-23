from math import sin, pi

def S(t, n, T):
    """The function S approximates the function t as n grows to infinity"""

    sinesum = 0
    for i in xrange(1, n + 1):
        sinesum += sin((2 * i - 1) * t) / (2 * i - 1)
    return (4 / pi) * sinesum

def f(t, T):
    """Piecewise function which S approximates"""

    if 0 <= t < T/2:
        value = 1
    elif t == T/2:
        value = 0
    elif T/2 < t <= T:
        value = -1
    return value

def diff_table(n_values, alpha_values, T):
    """Creates a list where every len(n) value corresponds to a change in alpha"""

    row = []
    for alpha in alpha_values:
        t = alpha * T
        for n in n_values:
            error = f(t, T) - S(t, n, T)
            row.append(error)
    return row

if __name__ == '__main__':
    """Function for using the module as a program"""

    import sys
    n_values = eval(sys.argv[1])
    alpha_values = eval(sys.argv[2])
    T = eval(sys.argv[3])
    print diff_table(n_values, alpha_values, T)
