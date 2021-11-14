from random import randrange
from fractions import Fraction as frac

n = 1000000  # one million (number of trials)
faces = 6  # of faces on die

def report():
    print(f'Monte Carlo result = {num_wounds / n:13.2%}')
    print(f'Analytic result = {str(analytic):>6} or {(analytic.numerator / analytic.denominator):.2%}')

def roll():
    return randrange(1, faces + 1)

print('No rerolls')

num_wounds = 0
for i in range(n // 4):
    # flamethrower
    for j in range(roll()):
        if roll() >= 3: num_wounds += 1
    # melta
    if roll() >= 4 and roll() >= 2: num_wounds += 2
# analytic = (frac(3, 6) + (frac(4 / 6) * frac(2 / 6))) / 2
flame = frac(4, 6) * frac(7, 2)  # 7/2 is the average result of rolling d6
melta = frac(5, 6) * frac(3, 6) * 2  # melta has 2 men for every 1 flamethrower
analytic = (flame + melta) / 4
report()

print('\nRerolls on hits')
num_wounds = 0
for i in range(n // 4):
    # flamethrower
    for j in range(roll()):
        if roll() >= 3: num_wounds += 1
    # melta
    first_reroll = True
    hits_roll = roll()
    if hits_roll >= 4 and roll() >= 2:
        num_wounds += 2
    elif hits_roll == 1 and first_reroll:
        first_reroll = False
        if roll() >= 4 and roll() > 2: num_wounds += 1
    # hits_reroll happens when hits roll = 1, i.e. 1/6 of the time
    # then it succeeds when roll() >= 2, i.e. 5/6 of the time
hits_reroll = frac(1, 6) * frac(5, 6) * 2  # 1/6 chance of reroll then regular
analytic += (hits_reroll / 2)  # only applies to melta, i.e. half the time
report()

print('\nRerolls on wounds')
num_wounds = 0
for i in range(n // 2):
    # flamethrower
    first_reroll = True
    flame_wound_roll = roll()
    if flame_wound_roll >= 3:  # wound roll
        num_wounds += 1
    elif flame_wound_roll == 1 and first_reroll:  # wound reroll
        first_reroll = False
        if roll() >= 3: num_wounds += 1
    # melta
    first_reroll = True
    melta_hit_roll = roll()
    melta_wound_roll = roll()
    if melta_hit_roll >= 4 and melta_wound_roll >= 2:
        num_wounds += 1
    elif first_reroll and roll() == 1:
        first_reroll = False
        if melta_wound_roll >= 2: num_wounds += 1
analytic -= (hits_reroll / 2)  # reset to original state
wound_reroll_flame = frac(1, 6) * flame
wound_reroll_melta = frac(1, 6) * melta
analytic += ((wound_reroll_flame + wound_reroll_melta) / 2)
report()
