import sys
from secant import secant
from math import *
from scitools.StringFunction import StringFunction

def newton(f, x, dfdx, N = 100, epsilon = 1.0E-4):
    """
    This function takes the function f, its derivative dfdx and uses
    a predefined epsilon value to check whether f(xn) < epsilon. Because the sequence might
    diverge, which would cause the loop to run forever, we need a maximum n value which is N.
    This function requires that you have the derivative of f(x)
    """

    f_value = f(x)
    root_approx = []
    n = 0

    while abs(f_value) > epsilon and n <= N:
        dfdx_val = float(dfdx(x))
        if abs(dfdx_val) < 1E-14:
            raise ValueError("Newton: f'(%g)=%g" % (x, dfdx_val))

        x = x - float(f_value/dfdx_val)
        root_approx.append(x)
        n += 1

        f_value = f(x)

    return root_approx

def bisection(f, a, b, epsilon = 1.0E-4):
    """
    The interval [a,b] is halved at m. If f(x) changes side in the left hand interval
    [a,m] the loop uses that interval and repeats. Otherwise the right hand interval
    [m,b] is chosen and the loop is repeated until the interval which is evaluated is
    smaller than epsilon. This function requires that you estimate an interval in which
    the root is located.
    """

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return []
    n = 0 # iteration counter

    m_list = []

    while b - a > epsilon:
        n += 1
        m = (a + b) / 2.0
        m_list.append(m)
        fm = f(m)
        if fa * fm <= 0:
            b = m # root is in left half of [a,b]
        else:
            a = m # root is in right half of [a,b]
            fa = fm
    return m_list

def pretty_print(name, values):
    for index, value in enumerate(values):
        print "%s: %.7f, n=%i" %(name, value, index)

if __name__ == '__main__':
    f = StringFunction(sys.argv[1])
    f_deriv = StringFunction(sys.argv[2])
    x0 = float(sys.argv[3])
    x1 = float(sys.argv[4])
    a = float(sys.argv[5])
    b = float(sys.argv[6])
    secant_n = int(sys.argv[7])

    pretty_print("newton", newton(f, x1, f_deriv))
    pretty_print("bisection", bisection(f, a, b))
    pretty_print("secant", secant(f, x0, x1, secant_n))


"""




[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'sin(x)' 'cos(x)' 1 4 1 4 25
newton: 2.8421787, n=0
newton: 3.1508729, n=1
newton: 3.1415924, n=2
bisection: 2.5000000, n=0
bisection: 3.2500000, n=1
bisection: 2.8750000, n=2
bisection: 3.0625000, n=3
bisection: 3.1562500, n=4
bisection: 3.1093750, n=5
bisection: 3.1328125, n=6
bisection: 3.1445312, n=7
bisection: 3.1386719, n=8
bisection: 3.1416016, n=9
bisection: 3.1401367, n=10
bisection: 3.1408691, n=11
bisection: 3.1412354, n=12
bisection: 3.1414185, n=13
bisection: 3.1415100, n=14
secant: 2.5794625, n=0
secant: 3.1664810, n=1
secant: 3.1402952, n=2
secant: 3.1415928, n=3
secant: 3.1415928, n=4
"""

"""
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'x - sin(x)' '1 - cos(x)' -1 1 -1 1 25
newton: 0.6551451, n=0
newton: 0.4335904, n=1
newton: 0.2881484, n=2
newton: 0.1918323, n=3
newton: 0.1278097, n=4
newton: 0.0851832, n=5
newton: 0.0567820, n=6
bisection: 0.0000000, n=0
bisection: -0.5000000, n=1
bisection: -0.2500000, n=2
bisection: -0.1250000, n=3
bisection: -0.0625000, n=4
bisection: -0.0312500, n=5
bisection: -0.0156250, n=6
bisection: -0.0078125, n=7
bisection: -0.0039062, n=8
bisection: -0.0019531, n=9
bisection: -0.0009766, n=10
bisection: -0.0004883, n=11
bisection: -0.0002441, n=12
bisection: -0.0001221, n=13
bisection: -0.0000610, n=14
secant: 0.0000000, n=0
secant: 0.0000000, n=1
"""

"""
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'x**5 - sin(x)' '5*x**4 - cos(x)' -0.5 0.5 -0.5 0.5 25
newton: -0.2931151, n=0
newton: 0.0184447, n=1
newton: -0.0000021, n=2
bisection: 0.0000000, n=0
bisection: -0.2500000, n=1
bisection: -0.1250000, n=2
bisection: -0.0625000, n=3
bisection: -0.0312500, n=4
bisection: -0.0156250, n=5
bisection: -0.0078125, n=6
bisection: -0.0039062, n=7
bisection: -0.0019531, n=8
bisection: -0.0009766, n=9
bisection: -0.0004883, n=10
bisection: -0.0002441, n=11
bisection: -0.0001221, n=12
bisection: -0.0000610, n=13
secant: 0.0000000, n=0
secant: 0.0000000, n=1
"""

"""
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'x**4 * sin(x)' '4*x**3 * sin(x) + x**4 * cos(x)' 2 6 2 6 25
newton: 6.3610517, n=0
newton: 6.2866767, n=1
newton: 6.2831930, n=2
newton: 6.2831853, n=3
bisection: 4.0000000, n=0
bisection: 3.0000000, n=1
bisection: 3.5000000, n=2
bisection: 3.2500000, n=3
bisection: 3.1250000, n=4
bisection: 3.1875000, n=5
bisection: 3.1562500, n=6
bisection: 3.1406250, n=7
bisection: 3.1484375, n=8
bisection: 3.1445312, n=9
bisection: 3.1425781, n=10
bisection: 3.1416016, n=11
bisection: 3.1411133, n=12
bisection: 3.1413574, n=13
bisection: 3.1414795, n=14
bisection: 3.1415405, n=15
secant: 2.1544982, n=0
secant: 2.3363957, n=1
secant: 1.2211590, n=2
secant: 1.1010205, n=3
secant: 0.8989049, n=4
secant: 0.7696981, n=5
secant: 0.6513865, n=6
secant: 0.5557978, n=7
secant: 0.4739534, n=8
secant: 0.4049575, n=9
secant: 0.3461686, n=10
secant: 0.2961190, n=11
secant: 0.2533971, n=12
secant: 0.2169069, n=13
secant: 0.1857100, n=14
secant: 0.1590254, n=15
secant: 0.1361904, n=16
secant: 0.1361904, n=17
"""

"""
newton: 3.0625000, n=0
newton: 2.4361367, n=1
newton: 2.1037680, n=2
newton: 2.0074282, n=3
newton: 2.0000411, n=4
newton: 2.0000000, n=5
bisection: 2.0000000, n=0
bisection: 1.0000000, n=1
bisection: 1.5000000, n=2
bisection: 1.7500000, n=3
bisection: 1.8750000, n=4
bisection: 1.9375000, n=5
bisection: 1.9687500, n=6
bisection: 1.9843750, n=7
bisection: 1.9921875, n=8
bisection: 1.9960938, n=9
bisection: 1.9980469, n=10
bisection: 1.9990234, n=11
bisection: 1.9995117, n=12
bisection: 1.9997559, n=13
bisection: 1.9998779, n=14
bisection: 1.9999390, n=15
secant: 0.2500000, n=0
secant: 0.4843214, n=1
secant: 73.5785532, n=2
secant: 0.4843611, n=3
secant: 0.4844009, n=4
secant: 35.5597214, n=5
secant: 0.4847507, n=6
secant: 0.4851004, n=7
secant: 35.4416874, n=8
secant: 0.4854537, n=9
secant: 0.4858069, n=10
secant: 35.2897189, n=11
secant: 0.4861647, n=12
secant: 0.4865225, n=13
secant: 35.1368035, n=14
secant: 0.4868850, n=15
secant: 0.4872474, n=16
secant: 34.9828190, n=17
secant: 0.4876147, n=18
secant: 0.4879819, n=19
secant: 34.8277465, n=20
secant: 0.4883540, n=21
secant: 0.4887261, n=22
secant: 34.6715657, n=23
secant: 0.4891032, n=24
"""

"""
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'x**10 - 1' '10*x**9' 3 10 0 3 25
newton: 9.0000000, n=0
newton: 8.1000000, n=1
newton: 7.2900000, n=2
newton: 6.5610000, n=3
newton: 5.9049000, n=4
newton: 5.3144100, n=5
newton: 4.7829690, n=6
newton: 4.3046722, n=7
newton: 3.8742052, n=8
newton: 3.4867852, n=9
newton: 3.1381080, n=10
newton: 2.8243006, n=11
newton: 2.5418793, n=12
newton: 2.2877139, n=13
newton: 2.0590008, n=14
newton: 1.8532510, n=15
newton: 1.6683137, n=16
newton: 1.5024812, n=17
newton: 1.3547959, n=18
newton: 1.2258196, n=19
newton: 1.1192392, n=20
newton: 1.0435975, n=21
newton: 1.0073465, n=22
newton: 1.0002365, n=23
newton: 1.0000003, n=24
bisection: 1.5000000, n=0
bisection: 0.7500000, n=1
bisection: 1.1250000, n=2
bisection: 0.9375000, n=3
bisection: 1.0312500, n=4
bisection: 0.9843750, n=5
bisection: 1.0078125, n=6
bisection: 0.9960938, n=7
bisection: 1.0019531, n=8
bisection: 0.9990234, n=9
bisection: 1.0004883, n=10
bisection: 0.9997559, n=11
bisection: 1.0001221, n=12
bisection: 0.9999390, n=13
bisection: 1.0000305, n=14
secant: 2.9999587, n=0
secant: 2.9999173, n=1
secant: 2.6999493, n=2
secant: 2.5393506, n=3
secant: 2.3496278, n=4
secant: 2.1880393, n=5
secant: 2.0325937, n=6
secant: 1.8900381, n=7
secant: 1.7569367, n=8
secant: 1.6336325, n=9
secant: 1.5192702, n=10
secant: 1.4136557, n=11
secant: 1.3167322, n=12
secant: 1.2290231, n=13
secant: 1.1518812, n=14
secant: 1.0878760, n=15
secant: 1.0406338, n=16
secant: 1.0128627, n=17
secant: 1.0021358, n=18
secant: 1.0001203, n=19
secant: 1.0000012, n=20
secant: 1.0000012, n=21
"""

"""
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'tanh(x)' '-(tanh(x))**2 + 1' -2 3 -2 3 25
Traceback (most recent call last):
  File "root_finder_examples.py", line 74, in <module>
    pretty_print("newton", newton(f, x1, f_deriv))
  File "root_finder_examples.py", line 21, in newton
    raise ValueError("Newton: f'(%g)=%g" % (x, dfdx_val))
ValueError: Newton: f'(-97.8566)=0
"""

"""
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'tanh(x) - x**(10)' '-10*x**9 -(tanh(x))**2' -2 3 -2 3 25
newton: 2.7000066, n=0
newton: 2.4300224, n=1
newton: 2.1870614, n=2
newton: 1.9684586, n=3
newton: 1.7718705, n=4
newton: 1.5953231, n=5
newton: 1.4373669, n=6
newton: 1.2974669, n=7
newton: 1.1768422, n=8
newton: 1.0797769, n=9
newton: 1.0136338, n=10
newton: 0.9818493, n=11
newton: 0.9731453, n=12
newton: 0.9717621, n=13
newton: 0.9715869, n=14
newton: 0.9715656, n=15
secant: -2.0883239, n=0
secant: -2.2280838, n=1
secant: -1.9348729, n=2
secant: -1.8401682, n=3
secant: -1.6945579, n=4
secant: -1.5802983, n=5
secant: -1.4661070, n=6
secant: -1.3619203, n=7
secant: -1.2626070, n=8
secant: -1.1678399, n=9
secant: -1.0741431, n=10
secant: -0.9759821, n=11
secant: -0.8600537, n=12
secant: -0.6878399, n=13
secant: -0.3286777, n=14
secant: 0.0475495, n=15
secant: -0.0014444, n=16
secant: 0.0000011, n=17
secant: 0.0000011, n=18
[Linueks@1x-193-157-241-123 oblig2]$ python root_finder_examples.py 'tanh(x) - x**(10)' '-10*x**9 -(tanh(x))**2' -2 3 -2 3 25
newton: 2.7000066, n=0
newton: 2.4300224, n=1
newton: 2.1870614, n=2
newton: 1.9684586, n=3
newton: 1.7718705, n=4
newton: 1.5953231, n=5
newton: 1.4373669, n=6
newton: 1.2974669, n=7
newton: 1.1768422, n=8
newton: 1.0797769, n=9
newton: 1.0136338, n=10
newton: 0.9818493, n=11
newton: 0.9731453, n=12
newton: 0.9717621, n=13
newton: 0.9715869, n=14
newton: 0.9715656, n=15
secant: -2.0883239, n=0
secant: -2.2280838, n=1
secant: -1.9348729, n=2
secant: -1.8401682, n=3
secant: -1.6945579, n=4
secant: -1.5802983, n=5
secant: -1.4661070, n=6
secant: -1.3619203, n=7
secant: -1.2626070, n=8
secant: -1.1678399, n=9
secant: -1.0741431, n=10
secant: -0.9759821, n=11
secant: -0.8600537, n=12
secant: -0.6878399, n=13
secant: -0.3286777, n=14
secant: 0.0475495, n=15
secant: -0.0014444, n=16
secant: 0.0000011, n=17
secant: 0.0000011, n=18
"""
