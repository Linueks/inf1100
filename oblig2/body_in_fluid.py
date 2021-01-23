import numpy as np
import matplotlib.pyplot as plt

g = 9.81
epsilon = 1.0e-7

def ForwardEuler(f, U0, T, n):
    """Solve u' = f(u, t), u(0) = U0, with n steps until t=T"""
    t = np.zeros(n+1)
    u = np.zeros(n+1) #u[k] is the solution at time t[k]

    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])

    return u, t #both of these are lists

class BodyFluid(object):
    def __init__(self, dragcoeff, fluid_dens, cross_sec, volume, body_dens):
        """
        dragcoeff, fluid density, cros section, volume, body density
        Drag coefficient is a dimensionless coefficient depending on the body's shape
        The fluid density is obvious
        The cross section is perpendicular to the motion, through the thickest part of the body
        """
        self.dragcoeff = dragcoeff
        self.fluid_dens = fluid_dens
        self.cross_sec = cross_sec
        self.volume = volume
        self.body_dens = body_dens
        self.g = g

    def __call__(self, init_velocity, t):
        g = self.g
        sigma = self.fluid_dens
        sigma_b = self.body_dens
        A = self.cross_sec
        V = self.volume
        C_D = self.dragcoeff

        return -g * (1 - sigma / sigma_b) - 0.5 * C_D * sigma * A\
                / (sigma_b * V) * abs(init_velocity) * init_velocity

def test_linear():
    bf = BodyFluid(1.0, 0.0, 1.0, 1.0, 1.0)
    V0 = 0 #m/s

    u_list, t_list = ForwardEuler(bf, V0, 10.0, 100)

    for i in xrange(len(u_list)):
        expected = (V0 - g * t_list[i])
        if abs(u_list[i] - expected) < epsilon:
            print 'yey, linear!'
        else:
            print 'something wrong'

def plot_forces():

    bf = BodyFluid(0.6, 0.79, 0.9, 0.08, 1003)
    fluid_dens = bf.fluid_dens
    body_dens = bf.body_dens
    volume = bf.volume
    dragcoeff = bf.dragcoeff
    cross_sec = bf.cross_sec
    mass = body_dens * volume

    g_force = -mass * g
    buoy_force = fluid_dens * g * volume
    drag_force = lambda u: -0.5 * dragcoeff * fluid_dens * cross_sec * abs(u) * u

    u_list, t_list = ForwardEuler(drag_force, 50.0, 1.0, 100)
    x_list = []
    y_list = []
    for i in xrange(len(u_list)):
        x_list.append(t_list[i])
        y_list.append(u_list[i])

    plt.plot(x_list, y_list, 'g-') #plotting drag_force
    plt.plot(x_list, [g_force for entry in y_list], 'r-') #plotting g_force
    plt.plot(x_list, [buoy_force for entry in y_list], 'b-') #plotting b_force
    plt.show()

def plot_skydiver():
    """Plotting velocity of skydiver in free fall through air"""
    bf = BodyFluid(0.6, 0.79, 0.9, 0.08, 1003.0)
    u_list, t_list = ForwardEuler(bf, 0, 20.0, 100)
    x_list = []
    y_list = []
    for i in xrange(len(u_list)):
        x_list.append(t_list[i])
        y_list.append(u_list[i])

    plt.plot(x_list, y_list)
    plt.show()

def plot_ball():
    r = 0.11
    mass = 0.43
    volume = 4.0 / 3.0 * np.pi * r ** 3
    body_dens = mass / volume

    bf = BodyFluid(0.2, 1000.0, np.pi*r**2, volume, body_dens)
    u_list, t_list = ForwardEuler(bf, 0, 1.0, 1000)
    x_list = []
    y_list = []
    for i in xrange(len(u_list)):
        x_list.append(t_list[i])
        y_list.append(u_list[i])

    plt.plot(x_list, y_list)
    plt.show()

#plot_ball()
#plot_skydiver()
#test_linear()
#plot_forces()
