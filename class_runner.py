from class_test import Weapon

# name, damage, num_shots
constant_weapon = Weapon('Constant', 2, 0)
variable_weapon = Weapon('Variable', 'D6', 0)

def show_damage(weapon):
    for i in range(5):
        print(f"{weapon.name} caused {weapon.damage_chooser(weapon.damage)} units of damage")

show_damage(constant_weapon)
print('\n')
show_damage(variable_weapon)
