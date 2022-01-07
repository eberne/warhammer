class Weapon:
    def __init__(self, name, weapon_type, attacks, s, ap, damage, plague=False, extra_attacks=0, unwieldy=False):
        self.name = name
        self.weapon_type = weapon_type
        self.attacks = attacks
        self.s = s  # strength
        self.ap = ap  # armor penetration
        self.damage = damage
        self.plague = plague
        self.extra_attacks = extra_attacks
        self.unwieldy = unwieldy
