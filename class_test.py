# import random
import random


class Unit:
    def __init__(self, name, num_people, person_list):
        self.name = name
        self.num_people = num_people
        self.person_list = person_list


class Person:
    def __init__(self, name, weapon_list):
        self.name = name
        self.weapon_list = weapon_list


class Weapon:
    def __init__(self, name, damage, num_shots):
        self.name = name
        self.damage = damage
        self.num_shots = num_shots

    @classmethod
    def damage_chooser(cls, damage):
        if damage == 'D6':
            return random.randint(1, 6)
        # insert other non-constant damage rules here if necessary
        return damage
