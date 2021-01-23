from __future__ import division
from ODEsolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt


"""
This is a program for solving the SIR ODE-system
S(t) defines how many of the population is susceptible
I(t) defines how many of the population is infected
R(t) defines how many of the population is recovered
"""

class SIR_equation:
    """
    Returns the right hand side of the equations;
    S'(t), I'(t), R'(t)
    """
    def __init__(self, v, dt, T, beta, S0, I0, R0):
        """
        v: probability of recovery per timestep
        dt: timestep
        T: number of days
        beta: probability of infection
        """
        self.v, self.dt, self.T, self.beta = v, dt, T, beta
        self.S0, self.I0, self.R0 = S0, I0, R0 #used to save initial values for terminate function

    def __call__(self, u, t):
        S, I, R = u                         #S, I, R are components of the vector u

        return [-self.beta*S*I,             #S'(t)
                 self.beta*S*I - self.v*I,  #I'(t)
                 self.v*I]                  #R'(t)

    def terminator(self, u, t, step_no):
        S, I, R = u[step_no]
        tolerance = 1.0e-7
        print S + I + R - (self.S0 + self.I0 + self.R0) > tolerance
        return S + I + R - (self.S0 + self.I0 + self.R0) > tolerance



def SIR_simulation(beta):
    v = 0.1
    init_S, init_I, init_R = 1500, 1, 0
    initial_conditions = [init_S, init_I, init_R]

    T = 365
    dt = 0.5
    n = T/dt

    f = SIR_equation(v, dt, T, beta, init_S, init_I, init_R)
    solver = RungeKutta4(f)
    solver.set_initial_condition(initial_conditions)
    time_points = np.linspace(0, 60, n+1)
    u, t = solver.solve(time_points, terminate=f.terminator)

    S, I, R = u[:,0], u[:,1], u[:,2]

    plt.plot(t, S,
             t, I,
             t, R)

    plt.xlabel('Days after outbreak')
    plt.ylabel('No. of people')
    plt.legend(['Susceptible', 'Infected', 'Resistant'])
    plt.show()


if __name__ == '__main__':
    SIR_simulation(0.0005)
    """
    When beta = 0.0005 the infection rate is much faster than when beta = 0.0001
    """
