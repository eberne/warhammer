class Weapon:
    def __init__(self, name, weapon_type, num_shots, s, ap, damage):
        self.name = name
        self.weapon_type = weapon_type
        self.num_shots = num_shots
        self.s = s  # strength
        self.ap = ap  # armor penetration
        self.damage = damage
