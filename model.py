class Model:
    def __init__(self, name, weapons, w, s, t, bs, ws, a, sv, quantity=1):
        self.name = name
        self.weapons = weapons
        self. w = w  # wounds
        self.s = s  # strength
        self.t = t  # toughness
        self.bs = bs  # ballistic skill
        self.ws = ws  # weapon skill
        self.a = a  # attacks
        self.sv = sv  # save
        self.quantity = quantity
