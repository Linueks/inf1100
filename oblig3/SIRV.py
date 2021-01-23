from SIR_class import ProblemSIR, SolverSIR
import numpy as np
import matplotlib.pyplot as plt
import ODEsolver

class ProblemSIRV(ProblemSIR):
    def __init__(self, v, beta, S0, I0, R0, V0, p, T):

        ProblemSIR.__init__(self, v, beta, S0, I0, R0, T) # let ProblemSIR store parameters
        self.V0 = V0                                      # initial no. people vaccinated
        self.p = p                                        # fraction of susceptibles vaccinated per dt

    def __call__(self, u, t):
        S, I, R, V = u

        return [                                # change in..
            -self.beta(t)*S*I - self.p*S,               # ..susceptible
             self.beta(t)*S*I - self.v(t)*I,    # ..infected
             self.v(t)*I,                       # ..resistant
             self.p*S                           # ..vaccinated
        ]                                       # persons per dt

class SolverSIRV(SolverSIR):
    def solve(self, method=ODEsolver.RungeKutta4):
        self.solver = method(self.problem)
        initial_conditions = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]
        self.solver.set_initial_condition(initial_conditions)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R, self.V = u[:,0], u[:,1], u[:,2], u[:,3]

    def plot(self):
        plt.plot(
            self.t, self.S,
            self.t, self.I,
            self.t, self.R,
            self.t, self.V
        )
        plt.xlabel('Days')
        plt.ylabel('no. of people')
        plt.legend(['Susceptible', 'Infected', 'Resistant', 'Vaccinated'])
        plt.show()

def test():
    #  S0 = initial healthy population
    #  I0 = initial infected population
    #  R0 = initial resistant population
    #  v0 = initial vaccinated population
    #  T  = duration (days)
    #beta = probability of infection per SI pair

    vaccine_problem = ProblemSIRV(beta=0.0005, v=0.1, S0=1500, I0=1, R0=0, V0=0, p=0.1, T=60)
    vaccine_sim = SolverSIRV(vaccine_problem, 0.5)
    vaccine_sim.solve()
    vaccine_sim.plot()
    print 'The maximum no. people infected now with vaccination:', int(vaccine_sim.calc_max())

    old_problem = ProblemSIR(beta=0.0005, v=0.1, S0=1500, I0=1, R0=0, T=60)
    simulation_old = SolverSIR(old_problem, 0.5)
    simulation_old.solve()
    print 'Compared to the old maximum no. of infected (beta=0.0005):', int(simulation_old.calc_max())

if __name__ == '__main__':
    test()
    """
    [Linueks@localhost oblig3]$ python SIRV.py
    The maximum no. people infected now with vaccination: 64
    Compared to the old maximum no. of infected (beta=0.0005): 897
    Complete vaccination has a huge effect... which is obvious...
    """
