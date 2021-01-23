from math import sin, pi

T = 2.0 * pi
nlist = [1, 3, 5, 10, 30, 100]
alpha = [0.01, 0.25, 0.49]

# a)
def S(t, n, T):
    """This function calculates S(t;n) which approximates f(t) via a partial sum"""


    sinesum = 0
    for i in xrange(1, n + 1):
        """
        Following function was a huge pain to deal with because the first term is always an interger division
        sinesum += (1 / (2 * i - 1)) * sin(2 * (2 * i - 1) * pi * t) was finally changed to what it is below
        and I got the correct result.
        """
        sinesum += sin((2 * i - 1) * t) / (2 * i -1)
    return (4 / pi) * sinesum

# b)
def f(t, T):
    """This is the piecewise function which S(t;n) approximates"""

    if 0 < t < T / 2:
        value = 1
    elif t == T / 2:
        value = 0
    elif T / 2 < t < T:
        value = -1
    return value

# c)
"""Creates a list where every len(n) value corresponds to a change in alpha"""
for a in alpha:
    row = []
    t = a * T
    for n in nlist:
        error = S(t, n, T) - f(t, T)
        row.append(error)


    print repr(row) + '\n'









"""
for i in range(0, 7):
    print 'Difference f(t) - S(t;n): '+ repr(f(alpha[i] * T, T) - S(alpha[i] * T, n[i], T))
"""

#Debugging
"""
print 'The value of t is 0 < t < T / 2, which returns: ' + repr(f(2.0, T))
print 'what S(t, n, T) returns: ' + repr(S(2.0, 10000, T))
print '------------------------------------------------'

print 'The value of t is T / 2 (pi) < t < T (2 * pi), which returns: ' + repr(f(3.20, T))
print 'what S(t, n, T) returns: ' + repr(S(3.20, 10000, T))
print '------------------------------------------------'

print 'The value of t == pi (T / 2), which returns: ' + repr(f(pi, T))
print 'what S(t, n, T) returns: ' + repr(S(pi, 10000, T))
print '------------------------------------------------'
"""
