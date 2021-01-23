from SIRV_varying_p import ProblemSIRV, SolverSIRV
import matplotlib.pyplot as plt

def optimal_duration():
    maximum_I = []
    time_points = range(0, 31, 1)
    for time in time_points:
        optimal_duration_problem = ProblemSIRV(p = lambda t: 0.1 if 6 <= t <= 6 + time else 0,
                                               beta=0.0005, v=0.1, S0=1500, I0=1, R0=0, V0=0, T=60)
        optimal_duration_sim = SolverSIRV(optimal_duration_problem, 0.5)
        optimal_duration_sim.solve()
        maximum_I.append(optimal_duration_sim.calc_max())

    return maximum_I

def plot(values):
    vaccination_time = []
    maximum_infected = []

    for vac_time, max_infected in enumerate(values):
        vaccination_time.append(vac_time)
        maximum_infected.append(max_infected)

    plt.plot(vaccination_time, maximum_infected)
    plt.show()

if __name__ == '__main__':
    plot(optimal_duration())
    print optimal_duration()
    """
    The number of infected converges to 441 after 9 days of vaccination, when beta=0.0005
    [Linueks@localhost oblig3]$ python SIRV_optimal_duration.py
    [877.35589758894105, 764.25790220192289, 669.12776810141145, 591.69267415980698,
     532.47707953201677, 490.46684184740479, 462.89122901853545, 447.73309998415226,
     441.94995442418212, 441.57841906399926, 441.57841906399926, 441.57841906399926,
     441.57841906399926, 441.57841906399926, 441.57841906399926, 441.57841906399926,
     441.57841906399926, 441.57841906399926, 441.57841906399926, 441.57841906399926,
     441.57841906399926, 441.57841906399926, 441.57841906399926, 441.57841906399926,
     441.57841906399926, 441.57841906399926, 441.57841906399926, 441.57841906399926,
     441.57841906399926, 441.57841906399926, 441.57841906399926]
    """
