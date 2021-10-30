from random import randrange
from fractions import Fraction as frac

n = 1000000  # one million (number to trials)
faces = 6  # of dice

def report():
    print(f'Monte Carlo result is {num_wounds * 100.0 / n:.2f} percent')
    print(f'Analytic result = {analytic} or {(analytic.numerator / analytic.denominator * 100):.2f} percent')

print('No rerolls')
num_wounds = 0
for i in range(n // 2):
    first_roll = randrange(1, faces + 1)
    # flamethrower
    if first_roll >= 3: num_wounds += 1
    # melta
    if first_roll >= 4:
        if randrange(1, faces + 1) >= 2: num_wounds += 1  # second roll
# analytic = (frac(3, 6) + (frac(4 / 6) * frac(2 / 6))) / 2
flame = frac(4, 6)
melta = frac(5, 6) * frac(3, 6)
analytic = (flame + melta) / 2
report()

print('\nRerolls on hits')
num_wounds = 0
for i in range(n // 2):
    first_roll = randrange(1, faces + 1)
    second_roll = randrange(1, faces + 1)
    reroll = randrange(1, faces + 1)
    # flamethrower
    if second_roll >= 3:
        num_wounds += 1
    # melta
    first_time = True
    if first_roll >= 4:
        if second_roll >= 2: num_wounds += 1
    elif first_roll == 1 and first_time:
        first_time = False
        if reroll >= 4 and second_roll >= 2: num_wounds += 1
# hit_reroll = 1/6 (1 on first roll) * melta (see above)
hit_reroll = frac(1, 6) * melta
analytic += (hit_reroll / 2)  # only applies to melta, i.e. half the time
decimal_analytic = analytic.numerator / analytic.denominator
report()

print('\nRerolls on wounds')
num_wounds = 0
for i in range(n // 2):
    first_roll = randrange(1, faces + 1)
    reroll = randrange(1, faces + 1)
    first_one = True
    # flamethrower
    if first_roll >= 3:
        num_wounds += 1
    elif first_roll == 1 and first_one:
        first_one = False
        if reroll >= 3: num_wounds += 1
    # melta
    first_roll = randrange(1, faces + 1)
    second_roll = randrange(1, faces + 1)
    reroll = randrange(1, faces + 1)
    first_one = True
    if first_roll >= 4:
        if second_roll >= 2:
            num_wounds += 1
        elif first_one:
            first_one = False
            if reroll >= 2: num_wounds += 1
analytic -= (hit_reroll / 2)  # reset to original state
wound_reroll_flame = frac(1, 6) * flame
wound_reroll_melta = frac(1, 6) * melta
analytic += ((wound_reroll_flame + wound_reroll_melta) / 2)
report()

