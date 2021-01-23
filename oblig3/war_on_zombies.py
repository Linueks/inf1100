from SIZR import *
import numpy as np
import matplotlib.pyplot as plt
import ODEsolver
from math import exp

def war_sim():
    beta = 0.03

    def alpha(t):
        w0 = 0.2*beta
        a = 50*w0
        small_sigma = 0.5
        w = 0.0
        T = [5.0, 10.0, 18.0]
        for i in range(len(T)):
            w += exp(-0.5*((t-T[i])/small_sigma)**2)
        w = a * w + w0
        return w

    problem = ProblemSIZR(sigma=0.0, beta=beta, delta_s=0.0, delta_i=0.0, p=1.0, alpha=alpha, S0=50.0, I0=0.0, Z0=3.0, R0=0.0, T=20)
    solver = SolverSIZR(problem, 0.5)
    solver.solve()
    solver.plot()

if __name__ == '__main__':
    war_sim()

"""
Repeated counter attacks by humans seem to kill off the zombies
"""
