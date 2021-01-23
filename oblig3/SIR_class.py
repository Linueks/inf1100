import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import ODEsolver

class ProblemSIR:
    def __init__(self, v, beta, S0, I0, R0, T):
        """
        v, beta: parameters in the ODE system
        S0, I0, R0: initial values
        T: simulaton for t in [0, T]
        """
        if isinstance(v, (float, int)):  # is v a number?
            self.v = lambda t: v         # wrap as function
        elif callable(v):
            self.v = v

        if isinstance(beta, (float, int)):  # is beta a number?
            self.beta = lambda t: beta      # wrap as function
        elif callable(beta):
            self.beta = beta

        self.S0, self.I0, self.R0 = S0, I0, R0
        self.T = T

    def __call__(self, u, t):
        """Right-hand-side function of the ODE system"""
        S, I, R = u
        return [
                -self.beta(t)*S*I,
                 self.beta(t)*S*I - self.v(t)*I,
                 self.v(t)*I
               ]

class SolverSIR:
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ODEsolver.RungeKutta4):
        self.solver = method(self.problem)
        initial_conditions = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(initial_conditions)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

    def old_plot(self):
        # first try at making plot
        plt.plot(
                self.t, self.S,
                self.t, self.I,
                self.t, self.R
                )
        plt.xlabel('Days')
        plt.ylabel('No. of people')
        plt.legend(['Susceptible', 'Infected', 'Resistant'])
        plt.show()

    def new_plot(self):
        # testing new things for creating plots
        plt.style.use("bmh")
        plt.figure(figsize=(12, 9))
        plt.title('Simulation of a disease spreading by a SIR model',
                    fontsize=22, fontstyle='normal')

        # removeing the plot frame lines
        ax = plt.subplot(111)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # adding 'legend' labels as i would on paper
        susceptible_label = self.S[-1]
        plt.text(61, susceptible_label, 'Susceptibles', fontsize='18')

        infected_label = self.I[-1]
        plt.text(61, infected_label, 'Infected', fontsize='18')

        resistant_label = self.R[-1]
        plt.text(61, resistant_label, 'Resistant', fontsize='18')

        # make sure axis ticks are large enough to be easily read
        plt.yticks(range(0, 1501, 300), fontsize=16)
        plt.xticks(range(0, 61, 20), fontsize=16)

        plt.ylim(0, 1500)
        plt.xlim(0, 74)

        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='on', left='off', right='off', labelleft='on')

        plt.plot(
                self.t, self.S,
                self.t, self.I,
                self.t, self.R
                )
        plt.show()


    def calc_max(self):
        return max(self.I)

def test():

    #  S0 = initial healthy population
    #  I0 = initial infected population
    #  R0 = initial resistant population
    #  T  = duration (days)
    #beta = probability of infection per SI pair

    problem_new = ProblemSIR(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
                             v=0.1, S0=1500, I0=1, R0=0, T=60)
    simulation_new = SolverSIR(problem_new, 0.5)
    simulation_new.solve()
    #simulation_new.old_plot()
    simulation_new.new_plot()
    print 'The maximum no. of people infected with hand washing campaign:', int(simulation_new.calc_max())


    problem_old = ProblemSIR(beta=0.0005, v=0.1, S0=1500, I0=1, R0=0, T=60)
    simulation_old = SolverSIR(problem_old, 0.5)
    simulation_old.solve()
    print 'Compared to the old maximum no. of infected (beta=0.0005):', int(simulation_old.calc_max())


if __name__ == '__main__':
    test()
    """
    [Linueks@localhost oblig3]$ python SIR_class.py
    The maximum no. of people infected with hand washing campaign: 745
    Compared to the old maximum no. of infected (beta=0.0005): 897
    """
