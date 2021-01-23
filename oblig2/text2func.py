from scitools.StringFunction import StringFunction
from math import *

def parsedesc(string):
    expr, rest = string.split(' is a function of ')
    var_and_params = rest.split(' with parameter ')
    func = StringFunction(expr, independent_variable=var_and_params[0])
    if len(var_and_params) > 1:
        parameters = eval("dict(%s)" % var_and_params[1])
        func.set_parameters(**parameters)
    return func

f = parsedesc('sin(a*y) is a function of y with parameter a=2')
print f
print f(2)

"""
[Linueks@1x-193-157-198-148 oblig2]$ python text2func.py
sin(2*y)
-0.756802495308
"""
