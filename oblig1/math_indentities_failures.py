import random
from math import sin, cos, sqrt, e, log, tan, sinh

n = 500
A = -100
B = 100

# a)
def power3_ident(A, B, n):
    """Function checks if the (a**3)*(b**3) == a**3"""
    failures_counter = 0
    for i in range(n):
        a = random.uniform(A, B); b = random.uniform(A, B)

        result1 = (a * b) ** 3
        result2 = (a ** 3) * (b ** 3)

        if result1 != result2:
            failures_counter += 1
    return repr((100.0 * failures_counter) / n) + '% failed'
"""
print power3_ident(-100, 100, 1000)
"""

#b
def equal(expr1, expr2, A = -100, B = 100, n = 500):
    """
    This function checks if mathematical identities hold on a computer
    expr1 and expr2 are both passed to the function as strings
    """

    failures_counter = 0

    for i in range(n):
        a = random.uniform(A, B); b = random.uniform(A, B)

        """
        If any of the generated a and b values are illegal for the expression
        this try except block will set the value to Null to prevent the program
        from getting ValueError
        """
        try:
            result1 = eval(expr1)
        except ValueError:
            result1 = None
        try:
            result2 = eval(expr2)
        except ValueError:
            result2 = None
        """
        This if block checks if both result1 and result2 are given valid numbers to work with
        """
        if result1 != None and result2 != None:
            if result1 != result2:
                failures_counter += 1

    return repr((100.0 * failures_counter) / n)

"""
print equal('(a*b)**3', '(a**3)*(b**3)', A, B, n)
print equal('e**(a + b)', '(e**a) * (e**b)', A, B, n)
print equal('log(a**b)', 'b * log(a)', A, B, n)
"""

#c
identities = [
    ['a - b','-(b - a)'],
    ['a / b', '1 / (b / a)'],
    ['(a * b ) ** 4', '(a ** 4) * (b ** 4)'],
    ['(a + b) ** 2', '(a ** 2) + (2 * a * b) + (b ** 2)'],
    ['(a + b) * (a - b)', '(a ** 2) - (b ** 2)'],
    ['e ** (a + b)', '(e ** a) * (e ** b)'],
    ['log(a ** b)', 'b * log(a)'],
    ['log(a * b)', 'log(a) + log(b)'],
    ['(a * b)', 'e ** (log(a) + log(b))'],
    ['1 / ((1 / a) + (1 / b))', '(a * b) / (a + b)'],
    ['a * ((sin(b)) ** 2 + (cos(b)) ** 2)', 'a'],
    ['sinh(a + b)', '((e ** a) * (e ** b) - (e ** (-a)) * (e ** (-b))) / 2'],
    ['tan(a + b)', '(sin(a + b)) / (cos(a + b))'],
    ['sin(a + b)', 'sin(a) * cos(b) + sin(b) * cos(a)']
]

"""Testing all the identities and writing it to file: 'math_identities_failures.txt'"""
with open('math_identities_failures.txt', 'w') as outfile:
    for i in range(len(identities)):
        outfile.write(identities[i][0] + ' = ' + identities[i][1] + '\n')
        outfile.write('A = 1, B = %3s; %4s%% failures' % ('2', equal(identities[i][0], identities[i][1], 1, 2)) + '\n')
        outfile.write('A = 1, B = 100; %4s%% failures' % equal(identities[i][0], identities[i][1], 1, 100) + '\n' + '\n')
