import matplotlib.pyplot as plt
import numpy as np
from numpy import asarray, poly1d, polyfit

with open('pendulum.dat', 'r') as infile:
    infile.readline()

    l_list = []
    t_list = []

    for line in infile:
        l_list.append(float(line.split()[0]))
        t_list.append(float(line.split()[1]))

l, t = np.asarray(l_list), np.asarray(t_list)

cof_1 = polyfit(l, t, 1)
cof_2 = polyfit(l, t, 2)
cof_3 = polyfit(l, t, 3)

print cof_1
print cof_2
print cof_3

poly1 = poly1d(cof_1)
poly2 = poly1d(cof_2)
poly3 = poly1d(cof_3)

#the cubic approximation fits best

plt.plot(
        l, t, 'bo',
        l, poly1(l), 'g-',
        l, poly2(l), 'b-',
        l, poly3(l), 'r-'
)
plt.legend(['data points',
            'linear approximation',
            'quadratic approximation',
            'cubic approximation'],
            loc='best')

plt.xlabel('T')
plt.ylabel('L')
plt.show()
