# the core rules for the game Warhammer 40,000 can be found at https://wahapedia.ru/wh40k9ed/the-rules/core-rules/
import random
from unit import Unit
from weapon import Weapon
import statistics
import pandas as pd

models = pd.read_csv('model_data.csv')
models.rename(index={0: 'plague_marine',
                     1: 'plague_marine_champion',
                     2: 'plague_marine_gunner',
                     3: 'intercessor',
                     4: 'intercessor_sergeant',
                     5: 'guardsman',
                     6: 'guardsman_sargent'},
              inplace=True)
models = models.T  # make models column names
print(models.plague_marine)
print(models.loc['Save', 'plague_marine'])

def d6():
    return random.randint(1, 6)

def d3():
    return random.randint(1, 3)

# Weapons
# 'name', weapon_type, attacks, strength, armor penetration, damage, plague, extra attacks, unweildy
bolt_gun = Weapon("Bolt Gun", "Rapid Fire", 1, 4, 0, 1)
blight_launcher = Weapon("Blight Launcher", "Assault", 2, 7, 2, 2, True)
bolt_rifle = Weapon("Bolt Rifle", "Rapid Fire", 1, 4, 1, 1)
plague_knife = Weapon("Plague Knife", "Melee", "User", "User", 1, 1, True)
power_sword = Weapon("Power Sword", "Melee", "User", "+1", 1, 1)
lasgun = Weapon("Lasgun", "Rapid Fire", 1, 3, 0, 1)
chainsword = Weapon("Chainsword", "Melee", "User", "User", 0, 1, extra_attacks=1)
lascannon = Weapon("Lascannon", "Heavy", 1, 9, 3, "d6")

# Units
# 'name', [models], Faction
plague_marines = Unit("Plague Marines",
                      [models.plague_marine_champion, models.plague_marine_gunner, models.plague_marine], "death_guard")
intercessors = Unit("Intercessors",
                    [models.intercessor_sergeant, models.intercessor], "Imperium")
infantry_squad = Unit("Infantry Squad", [models.guardsman, models.guardsman_sargent], "astra_militarum")

def get_hits(attacker, weapon):
    hit_mod = 0
    hits = 0
    if weapon.weapon_type == "Heavy":
        moved = True  # input("Moved with heavy? (y/n)")
        if moved: hit_mod += 1
    elif weapon.weapon_type == "Assault":
        advanced = True  # input("Advanced? (y/n)")
        if advanced: hit_mod += 1
    if weapon.unwieldy:
        hit_mod += 1
    if hit_mod > 1:
        hit_mod = 1
    elif hit_mod < -1:
        hit_mod = -1
    if weapon.weapon_type == "Melee":
        hit_check = attacker.ws
    else:
        hit_check = attacker.bs
    hit_check += hit_mod
    if weapon.attacks == "User":
        attacks = attacker.attacks + weapon.extra_attacks
    else:
        attacks = weapon.attacks + weapon.extra_attacks
    if weapon.weapon_type == "Rapid Fire":
        moved = False  # input("Did you move? (y/n)")
        if not moved: attacks *= 2
    for i in range(attacks):
        if d6() >= hit_check:
            hits += 1
    return hits

def get_wounds(attacker, defender, weapon, hits):
    #    returns number of wounds
    wound_check = 0
    wounds = 0
    strength = weapon.s
    t_lst = []
    for i in defender.models:
        for j in range(i.quantity):
            t_lst.append(i.t)
    toughness = statistics.mode(t_lst)
    if type(strength) == str:
        if strength == "User":
            strength = attacker.s
        elif strength[0] == "+":
            strength = attacker.s + int(strength[1])
        elif strength[0] == "*":
            strength = attacker.s * int(strength[1])
    if strength == toughness:
        wound_check = 4
    elif strength > toughness:
        wound_check = 3
    elif strength >= 2 * toughness:
        wound_check = 2
    elif strength < toughness:
        wound_check = 5
    elif strength * 2 <= toughness:
        wound_check = 6
    for i in range(hits):
        if d6() >= wound_check:
            wounds += 1
    return wounds

def get_saves(defender, weapon, wounds):
    # returns number of failed saves
    save_check = defender.models[0].sv + weapon.ap
    failed_saves = 0
    for i in range(wounds):
        if d6() < save_check:
            failed_saves += 1
    return failed_saves

def get_damage(defender, weapon, f_saves):
    deaths = 0
    damage = 0
    for i in range(f_saves):
        damage += weapon.rand_damage(weapon.damage)
        # print(damage)
        if damage >= defender.models[0].w:
            damage = 0
            deaths += 1

    return deaths, damage

attacker_datasheet = intercessors
defender_datasheet = infantry_squad
attacker_weapon = bolt_rifle
failed_save_num = 0

for model in attacker_datasheet.models:
    for model_num in range(7):
        hit_num = get_hits(model, attacker_weapon)
        wound_num = get_wounds(model, defender_datasheet, attacker_weapon, hit_num)
        failed_save_num += get_saves(defender_datasheet, attacker_weapon, wound_num)
dead_models = get_damage(defender_datasheet, attacker_weapon, failed_save_num)
if dead_models[1] == 0:
    print(f"deaths: {dead_models[0]}")
else:
    print(f"deaths: {dead_models[0]}\nwounds remaining: {defender_datasheet.models[0].w - dead_models[1]}")

# TODO:
#  1. add shooting w/ multiple weapons
#  2. add reroll capabilities
#  3. add more differing profiles
#  4. add framework for gathering data
#  5. make Quantity an int
