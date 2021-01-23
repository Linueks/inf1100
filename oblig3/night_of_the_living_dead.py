from SIZR import *
from scitools.std import PiecewiseConstant

def night_of_the_living_dead():
    first_phase_duration = 4.0
    second_phase_duration = first_phase_duration + 24.0
    third_phase_duration = second_phase_duration + 5.0

    sigma = PiecewiseConstant(domain=[0, third_phase_duration],
                              data=[(0.0, 20.0), (4.0, 2.0), (28.0, 0.0)])

    beta = PiecewiseConstant(domain=[0, third_phase_duration],
                              data=[(0.0, 0.03), (4.0, 0.0012), (28.0, 0.0)])

    p = PiecewiseConstant(domain=[0, third_phase_duration],
                              data=[(0.0, 1.0), (4.0, 1.0), (28.0, 1.0)])

    alpha = PiecewiseConstant(domain=[0, third_phase_duration],
                              data=[(0.0, 0.0), (4.0, 0.0016), (28.0, 0.006)])

    delta_i = PiecewiseConstant(domain=[0, third_phase_duration],
                              data=[(0.0, 0.0), (4.0, 0.014), (28.0, 0.0)])

    delta_s = PiecewiseConstant(domain=[0, third_phase_duration],
                              data=[(0.0, 0.0), (4.0, 0.0), (28.0, 0.0067)])

    problem = ProblemSIZR(sigma, beta, delta_s, delta_i, p, alpha, 60, 0, 1, 0, third_phase_duration)
    solver = SolverSIZR(problem, 0.5)
    solver.solve()
    solver.plot()

if __name__ == '__main__':
    """seems weird to have sigma=20 for the first 4 hours..."""
    night_of_the_living_dead()
