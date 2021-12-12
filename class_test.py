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
    def __init__(self, damage, num_shots):
        self.damage = damage
        self.num_shots = num_shots
