import matplotlib.pyplot as plt
import numpy as np
import ODEsolver


def make_function(thing):
    if isinstance(thing, (float, int)):
        return lambda t: thing
    elif callable(thing):
        return thing

class ProblemSIZR:
    def __init__(self, sigma, beta, delta_s, delta_i, p, alpha, S0, I0, Z0, R0, T):
                        # initial amount of ..
        self.S0 = S0    # .. susceptibles
        self.I0 = I0    # .. infected
        self.Z0 = Z0    # .. zombies
        self.R0 = R0    # .. removed (either killed zombies or humans)
        self.T = T      # duration (hours)

        for parameter in ['sigma', 'beta', 'delta_s', 'delta_i', 'p', 'alpha']:
            setattr(self, parameter, make_function(vars()[parameter]))

    def __call__(self, u, t):
        S, I, Z, R = u

                                    # interpretation of parameters ..
        sigma = self.sigma          # .. number of new humans brought into zombified area per dt
        beta = self.beta            # .. probability that human-zombie pair meets, during a dt, and human getting infected
        delta_s = self.delta_s      # .. probability that a susceptible human is killed or dies in a dt
        delta_i = self.delta_i      # .. probability that an infected human is killed or dies in a dt
        p = self.p                  # .. probability that an infected human is turned into a zombie in a dt
        alpha = self.alpha          # .. probability that human-zombie pair fights, during a dt, and zombie is killed


        return [                                            # change in ..
            sigma(t) - beta(t)*S*Z - delta_s(t)*S,          # .. susceptibles
            beta(t)*S*Z - p(t)*I - delta_i(t)*I,            # .. infected
            p(t)*I - alpha(t)*S*Z,                          # .. zombies
            delta_s(t)*S + delta_i(t)*I + alpha(t)*S*Z      # .. removed
        ]                                                   # persons per dt

class SolverSIZR:
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ODEsolver.RungeKutta4):
        self.solver = method(self.problem)
        initial_conditions = [self.problem.S0, self.problem.I0, self.problem.Z0, self.problem.R0]
        self.solver.set_initial_condition(initial_conditions)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.Z, self.R = u[:,0], u[:,1], u[:,2], u[:,3]

    def plot(self):
        plt.plot(
            self.t, self.S,
            self.t, self.I,
            self.t, self.Z,
            self.t, self.R
        )
        plt.xlabel('time')
        plt.ylabel('no. of people')
        plt.legend(['Susceptible', 'Infected', 'Zombies', 'Removed'])
        plt.show(block=True)

def test():
    hysterical_phase = ProblemSIZR(
                                       sigma=2.0, beta=0.0012, delta_s=0.0,
                                       delta_i=0.014, p=1.0, alpha=0.0016,
                                       S0=10.0, I0=0.0, Z0=100.0, R0=0.0, T=24
                                   )
    h_p_simulation = SolverSIZR(hysterical_phase, 0.5)
    h_p_simulation.solve()
    h_p_simulation.plot()

if __name__ == '__main__':
    test()
