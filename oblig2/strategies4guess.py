import random

def midpoint_strat(p, q):
    return (p + q) / 2

def uniform_strat(p, q):
    return random.randint(p, q)

def the_gamev2(strategy):
    """Uses the strategies defined above to guess the secret number"""
    p, q = 1, 100
    secret_number = random.randint(p, q)
    attempts = 0
    guess = 0

    while guess != secret_number:
        guess = strategy(p, q)
        attempts += 1

        if guess < secret_number:
            p = guess + 1
        elif guess > secret_number:
            q = guess - 1
    return attempts

"""Testing the two strategies 10000 times and taking average"""
N = 10000
midpoint_avg_result = 0.0
uniform_avg_result = 0.0

for i in xrange(N):
    midpoint_avg_result += the_gamev2(midpoint_strat)
    uniform_avg_result += the_gamev2(uniform_strat)

midpoint_avg_result = midpoint_avg_result / N
uniform_avg_result = uniform_avg_result / N

print 'midpoint:', midpoint_avg_result
print 'uniform:', uniform_avg_result


"""
[Linueks@1x-193-157-198-148 oblig2]$ python strategies4guess.py
midpoint: 5.7816
uniform: 7.4851
"""
