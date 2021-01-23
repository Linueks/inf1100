import ODEsolver as ode
import numpy as np
import matplotlib.pyplot as plt
from body_in_fluid import BodyFluid
from math import copysign

class TermBodyFluid(BodyFluid):
    def terminal_velocity_equation(self):
        sigma = self.fluid_dens
        sigma_b = self.body_dens
        C_d = self.dragcoeff
        V = self.volume
        g = self.g
        A = self.cross_sec

        return -np.sqrt(2.0 * g * (1 - sigma / sigma_b) / (C_d * sigma * A) * (sigma_b * V))

def terminator(u, t, step_no):
    """returns true for stopping the solver"""
    tolerance = 1.0e-4
    value = abs(u[step_no] - u[step_no - 1]) <= tolerance
    return value

def term_velocity_skydiver():
    """plotting the terminal velocity of the skydiver with the exact velocity"""
    tbf = TermBodyFluid(0.6, 0.79, 0.9, 0.08, 1003)
    termvel = tbf.terminal_velocity_equation()
    solver = ode.RungeKutta4(tbf)
    solver.set_initial_condition(0.0)

    n_list = range(10, 100, 5)
    velocity_calcs = []
    """making the t_major list to make sure of equal versions of lists being plotted"""
    t_major = []

    for n in n_list:
        t_list = np.linspace(0.0, 100.0, n)
        t_major.append(t_list)

        solver.solve(t_list, terminate=terminator)
        velocity_calcs.append(solver.u)

    plt.plot(t_list, [termvel for _ in solver.u])
    plt.plot(t_major[-1], velocity_calcs[-1])
    plt.show()

def term_velocity_ball():
    """plotting the terminal velocity of the ball with the exact terminal velocity"""
    r = 0.11
    m = 0.43
    A = np.pi * r**2
    V = 4.0 / (3.0*np.pi*r**3)
    sigma_b = m / V

    tbf = TermBodyFluid(0.2, 1000, A, V, sigma_b)
    termvel = tbf.terminal_velocity_equation()
    solver = ode.RungeKutta4(tbf)
    solver.set_initial_condition(0.0)

    n_list = range(10, 100, 5)
    velocity_calcs = []
    t_major = []

    for n in n_list:
        t_list = np.linspace(0.0, 100.0, n)
        t_major.append(t_list)

        solver.solve(t_list, terminate=terminator)
        velocity_calcs.append(solver.u)

    plt.plot(t_list, [termvel for _ in solver.u])
    plt.plot(t_major[-1], velocity_calcs[-1])
    plt.show()


term_velocity_skydiver()
term_velocity_ball()
