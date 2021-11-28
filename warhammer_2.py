from random import randrange
from fractions import Fraction as frac

num_rounds = 100000  # one million


def report():
    print(f'Monte Carlo result = {(total_score / 10) / num_rounds:14.2%}')
    print(f'Analytic result = {str(analytic):>7} or {(analytic.numerator / analytic.denominator):.2%}')


def roll():
    return randrange(1, 7)


print("Base Case")
total_score = 0
for i in range(num_rounds):
    # flamethrower
    for j in range(roll()):
        if roll() >= 3:
            total_score += 1

    # meltagun
    hit_roll = roll()
    if hit_roll >= 4 and roll() >= 2:
        total_score += 4

''' Analysis of probability
Flamethrowers number of rolls = 7/2 which is average roll of six sided dice
    on each roll they score 3+ which has a probability of 4/6
Meltaguns get 4 rolls per turn
    to score they must roll 4+, probability of 3/6 and 2+, probability of 5/6
'''
analytic = (frac(4, 6) * frac(7, 2) + frac(5, 6) * frac(3, 6) * 4) / 10
report()

print("\nReroll on hit")
total_score = 0
for i in range(num_rounds):
    # flamethrower - same as base case
    for j in range(roll()):
        if roll() >= 3: total_score += 1

    # meltagun - do reroll if hit_roll == 1
    hit_roll = roll()
    if hit_roll >= 4:
        if roll() >= 2: total_score += 4
    elif hit_roll == 1:  # reroll
        if roll() >= 4 and roll() >= 2: total_score += 4

analytic += (frac(1, 6) * frac(5, 6) * frac(3, 6) * 4) / 10
report()

print("\nReroll on wound")
total_score = 0
for i in range(num_rounds):
    # flamethrower
    for j in range(roll()):
        wound_roll = roll()
        if wound_roll >= 3:
            total_score += 1
        elif wound_roll == 1:
            if roll() >= 3: total_score += 1

    # meltagun
    wound_roll = roll()
    if roll() >= 4 and wound_roll > 2:
        total_score += 4
    elif wound_roll == 1:
        if roll() >= 4 and roll() >= 2: total_score += 4

analytic += (frac(1, 6) * frac(3, 6)) / 10
report()
