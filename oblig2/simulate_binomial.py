from math import factorial
import random

def binomial(x, n, p):
    result = (factorial(n) * (p**x) * (1 - p) ** (n - x)) / (factorial(x) * factorial(n - x))
    return result

def simulate_binomial(x, n, p, N=10000):
    M = 0
    for test in xrange(N):
        counter = 0
        rnd = random.Random()
        for i in xrange(n):
            if rnd.uniform(0, 1) <= p:
                counter += 1
        if counter == x:
            M += 1

    simulated_result = float(M) / N
    exact_result = binomial(x, n, p)

    return simulated_result, exact_result

def simulation_test():
    """Tests the simulate_binomial function with problems from 4.23 b), c), d)"""

    #Test for 4.23b)
    x, n, p = 2, 5, 0.5
    sim, exact = simulate_binomial(x, n, p)
    print 'coinflip, simulated: %.7f, exact: %.7f' % (sim, exact)

    #Test for 4.23c)
    x, n, p = 4, 4, 1.0/6.0
    sim, exact = simulate_binomial(x, n, p)
    print 'dice, simulated: %.7f, exact: %.7f' % (sim, exact)

    #Test for 4.23d)
    x, n, p = 0, 5, 1.0/120.0
    sim, exact = simulate_binomial(x, n, p)
    print 'skiers, simulated: %.7f, exact: %.7f' % (sim, exact)

simulation_test()

"""
Run example:

[Linueks@localhost oblig2]$ python simulate_binomial.py
coinflip, simulated: 0.3076000, exact: 0.3125000
dice, simulated: 0.0008000, exact: 0.0007716
skiers, simulated: 0.9560000, exact: 0.9590220
"""
