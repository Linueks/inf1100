"""This program has the added functionality of being able to pass values to
the diff_table function from the command line"""

import argparse as ap
from sinesum2 import diff_table
from math import pi

parser = ap.ArgumentParser()

parser.add_argument(
    '-n',
    type = eval,
    default = [1,3,5,10,100],
    help = 'numbers of iterations',
    metavar = 'n'
)

parser.add_argument(
    '-alpha',
    type = eval,
    default = [0.10,0.25,0.49],
    help = 'variation factor for t',
    metavar = 'a'
)

parser.add_argument(
    '-T',
    type = eval,
    default = 2 * pi,
    help = 'constant equal to 2 * pi',
    metavar = 'T'
)

args = parser.parse_args()

print str(diff_table(args.n, args.alpha, args.T)) [1:-1]
