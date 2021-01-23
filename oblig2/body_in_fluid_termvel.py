from body_in_fluid import BodyFluid
import ODEsolver as ode
import matplotlib.pyplot as plt
import numpy as np
from math import copysign

class TermBodyFluid(BodyFluid):
    def terminal_velocity(self):
        g = self.g
        sigma = self.fluid_dens
        sigma_b = self.body_dens
        A = self.cross_sec
        V = self.volume
        C_D = self.dragcoeff

        inside_root = -2.0 * g * (1 - sigma / sigma_b) / (C_D * sigma * A) * (sigma_b * V)
        sign = copysign(1, inside_root)
        return sign * np.sqrt(abs(inside_root))

def end(self, u, step_no):
    """Return True when terminal velocity is reached"""
    tolerance = 1.0e-4
    return abs(u[step_no] - u[step_no - 1]) <= tolerance

def skydiver_termvel():
    tbf = TermBodyFluid(0.6, 0.79, 0.9, 0.08, 1003)
    termvel = tbf.terminal_velocity()

    n_list = range(10, 1000, 10)
    termvel_calcs = []

    for n_val in n_list:
        solver = ode.RungeKutta4(tbf)
        solver.set_initial_condition(0.0)
        t_list = np.linspace(0, 100.0, n_val)
        termvel_calc, _ = solver.solve(t_list, terminate=end)
        termvel_calcs.append(termvel_calc[-1])

    plt.plot(n_list, termvel_calcs, 'r-')
    plt.plot(n_list, [termvel for x in n_list])
    plt.show()

def ball_termvel():
    r = 0.11
    m = 0.43
    A = np.pi * r * r
    V = 4.0 / (3.0*np.pi*r**3)
    sigma_b = m / V

    tbf = TermBodyFluid(0.2, 1000, A, V, sigma_b)
    termvel = tbf.terminal_velocity()

    n_list = range(10, 1000, 10)
    termvel_calcs = []

    for n_val in n_list:
        solver = ode.RungeKutta4(tbf)
        solver.set_initial_condition(0.0)
        t_list = np.linspace(0, 100.0, n_val)
        termvel_calc, _ = solver.solve(t_list, terminate=end)
        termvel_calcs.append(termvel_calc[-1])

    print termvel_calcs
    plt.plot(n_list, termvel_calcs, 'r-')
    plt.plot(n_list, [termvel for x in n_list])
    plt.show()

skydiver_termvel()
ball_termvel()
