# the core rules for the game Warhammer 40,000 can be found at https://wahapedia.ru/wh40k9ed/the-rules/core-rules/
import random
from unit import Unit
from weapon import Weapon
from model import Model

# Weapons
# 'name', weapon_type, attacks, strength, armor penetration, damage, plague, extra attacks
bolt_gun = Weapon("Bolt Gun", "Rapid Fire", 1, 4, 0, 1)
blight_launcher = Weapon("Blight Launcher", "Assault", 2, 7, 2, 2, True)
bolt_rifle = Weapon("Bolt Rifle", "Rapid Fire", 1, 4, 1, 1)
plague_knife = Weapon("Plague Knife", "Melee", None, "User", 1, 1, True)
power_sword = Weapon("Power Sword", "Melee", "User", "+1", 1, 1)
lasgun = Weapon("Lasgun", "Rapid Fire", 1, 3, 0, 1)
chainsword = Weapon("Chainsword", "Melee", "User", "User", 0, 1, extra_attacks=1)

# print(plague_knife.__dict__)

# Models
# 'name', [weapons], wounds, strength, toughness, ballistic skill, weapon skill, attacks, save, quantity
plague_marine = Model("Plague Marine", [bolt_gun, plague_knife], 2, 4, 5, 3, 3, 2, 3, 3)
plague_marine_champion = Model("Plague Marine Champion", [bolt_gun, plague_knife, power_sword], 2, 4, 5, 3, 3, 3, 3)
plague_marine_gunner = Model("Plague Marine Gunner", [blight_launcher, plague_knife], 2, 4, 5, 3, 3, 2, 3)
intercessor = Model("Intercessor", [bolt_rifle], 2, 4, 4, 3, 3, 2, 3, 4)
intercessor_sergeant = Model("Intercessor Sergeant", [bolt_rifle, power_sword], 2, 4, 4, 3, 3, 3, 3)
guardsman = Model("Guardsman", [lasgun], 1, 3, 3, 4, 4, 1, 5, 9)
guardsman_sergeant = Model("Guardsman Sergeant", [lasgun, chainsword], 1, 3, 3, 4, 4, 2, 5)

# Units
# 'name', [models], Faction
plague_marines = Unit("Plague Marine",
                      [plague_marine_champion, plague_marine_gunner, plague_marine, plague_marine,
                       plague_marine], "death_guard")
intercessors = Unit("Intercessors",
                    [intercessor_sergeant, intercessor, intercessor, intercessor, intercessor], "Imperium")
infantry_squad = Unit("Infantry Squad", [guardsman, guardsman_sergeant], "astra_militarum")


def d6():
    return random.randint(1, 6)


def d3():
    return random.randint(1, 3)


def get_hits(attacker, weapon, defender):
    pass


def get_wounds(attacker, defender, weapon, hits):
    pass


def get_saves(attacker, defender, weapon, wounds):
    pass


def get_damage(attacker, defender, weapon, saves):
    pass


