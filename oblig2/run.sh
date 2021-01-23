#!/bin/sh

python root_finder_examples.py 'sin(x)' 'cos(x)' 1 4 1 4 25
python root_finder_examples.py 'x - sin(x)' '1 - cos(x)' -1 1 -1 1 25
python root_finder_examples.py 'x**5 - sin(x)' '5*x**4 - cos(x)' -0.5 0.5 -0.5 0.5 25
python root_finder_examples.py 'x**4 * sin(x)' '4*x**3 * sin(x) + x**4 * cos(x)' 2 6 2 6 25
python root_finder_examples.py 'x**4 - 16' '4*x**3' 0 4 0 4 25
python root_finder_examples.py 'x**10 - 1' '10*x**9' 0 3 0 3 25
python root_finder_examples.py 'tanh(x)' '-(tanh(x))**2 + 1' -2 2 -2 2 25
python root_finder_examples.py 'tanh(x) - x**(10)' '-10*x**9 -(tanh(x))**2' -2 2 -2 2 25
