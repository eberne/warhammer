# the core rules for the game Warhammer 40,000 can be found at https://wahapedia.ru/wh40k9ed/the-rules/core-rules/
import random
from unit import Unit
from weapon import Weapon
from model import Model
from faction import Faction

# Weapons
# 'name', weapon_type, num_shots, strength, armor penetration, damage
bolt_gun = Weapon("Bolt Gun", "Rapid Fire", 1, 4, 0, 1)
blight_launcher = Weapon("Blight Launcher", "Assault", 2, 7, 2, 2)
bolt_rifle = Weapon("Bolt Rifle", "Rapid Fire", 1, 4, 1, 1)
plague_knife = Weapon("Plague Knife", "Melee", None, "User", 1, 1)
plague_knife.attacks = "User"
plague_knife.plague = True
power_sword = Weapon("Power Sword", "Melee", "User", "+1", 1, 1)
# print(plague_knife.__dict__)

# Models
# 'name', [weapons], wounds, strength, toughness, ballistic skill, weapon skill, attacks, save
plague_marine = Model("Plague Marine", [bolt_gun, plague_knife], 2, 4, 5, 3, 3, 2, 3)
plague_marine_champion = Model("Plague Marine Champion", [bolt_gun, plague_knife, power_sword], 2, 4, 5, 3, 3, 3, 3)
plague_marine_gunner = Model("Plague Marine Gunner", [blight_launcher, plague_knife], 2, 4, 5, 3, 3, 2, 3)
intercessor = Model("Intercessor", [bolt_rifle], 2, 4, 4, 3, 3, 2, 3)
intercessor_sergeant = Model("Intercessor Sergeant", [bolt_rifle, power_sword], 2, 4, 4, 3, 3, 3, 3)

# Factions
# 'name', sargent, sargent_war_gear (sargent and sargent_war_gear are boolean)
death_guard = Faction("Death Guard", True, True)
astra_militarum = Faction("Astra Militarum", True, True)

# Units
# 'name', [models], Faction
plague_marines = Unit("Plague Marine",
                      [plague_marine_champion, plague_marine_gunner, plague_marine, plague_marine,
                       plague_marine], death_guard)
intercessors = Unit("Intercessors",
                    [intercessor_sergeant, intercessor, intercessor, intercessor, intercessor], "Imperium")
guardsmen = Unit("Guardsmen", [], astra_militarum)

def d6():
    return random.randint(1, 6)

def d3():
    return random.randint(1, 3)

deaths_list = []
wound_list = []

# datasheets = {
# "Plague Marine": {"M": 5, "WS": 3, "BS": 3, "S": 4, "T": 5, "W": 2, "A": 2, "Ld": 7, "Sv": 3, "Size": 4}
#    "Faction": "death_guard", "Sergeant": True, "Sergeant war_gear": True,
#     "Weapons": {
#         "Bolt_gun": {"Type": "Rapid Fire", "Attacks": 1, "Range": 30, "Strength": 4, "AP": 0,
#                     "Damage": 1, "Plague": False, "sWeapon": False},
#         "Plague Knife": {"Type": "Melee", "Attacks": "User", "Range": "Melee", "Strength": "User",
#                          "AP": 1, "Damage": 1, "Plague": True, "sWeapon": False, "Unwieldy": False},
#         "Power Fist": {"Type": "Melee", "Attacks": "User", "Range": "Melee", "Strength": "2*",
#                        "AP": 3, "Damage": 2, "Plague": False, "sWeapon": True, "Unwieldy": True}}},
# "Intercessor": {"M": 6, "WS": 3, "BS": 3, "S": 4, "T": 4, "W": 2, "A": 2, "Ld": 7, "Sv": 3,
#                                   "Size": 4,
#                                   "Faction": "Space Marines", "Sergeant": True, "Sergeant Wargear": True,
#                                   "Weapons": {
#                                       "Bolt Rifle": {"Type": "Rapid Fire", "Attacks": 1, "Range": 30, "Strength": 4,
#                                                      "AP": 1,
#                                                      "Damage": 1, "sWeapon": False},
#                                       "Close Combat Weapon": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                               "Strength": "User", "AP": 0, "Damage": 1,
#                                                               "sWeapon": False,
#                                                               "Unwieldy": False},
#                                       "Power Sword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                       "Strength": "1+", "AP": 3,
#                                                       "Damage": 1, "sWeapon": True, "Unwieldy": False},
#                                       "Power Fist": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                      "Strength": "2*", "AP": 3,
#                                                      "Damage": 2, "sWeapon": True, "Unwieldy": True}}},
#                   "Guardsmen": {"M": 6, "WS": 4, "BS": 4, "S": 3, "T": 3, "W": 1, "A": 1, "Ld": 6, "Sv": 5,
#                                 "Size": 4,
#                                 "Faction": "Astra Militarum", "Sergeant": True, "Sergeant Wargear": True,
#                                 "Weapons": {
#                                     "Lasgun": {"Type": "Rapid Fire", "Attacks": 1, "Range": 18, "Strength": 3,
#                                                "AP": 0,
#                                                "Damage": 1, "sWeapon": False},
#                                     "Close Combat Weapon": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                             "Strength": "User",
#                                                             "AP": 0, "Damage": 1, "sWeapon": False,
#                                                             "Unwieldy": False},
#                                     "Chainsword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                    "Strength": "User",
#                                                    "AP": 1, "Damage": 1, "sWeapon": True, "Unwieldy": False},
#                                     "Power Sword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                     "Strength": "1+",
#                                                     "AP": 3, "Damage": 1, "sWeapon": True, "Unwieldy": False}}},
#                   "Eradicator": {"M": 5, "WS": 3, "BS": 3, "S": 4, "T": 5, "W": 3, "A": 2, "Ld": 7, "Sv": 3,
#                                  "Size": 2,
#                                  "Faction": "Space Marines", "Sergeant": True, "Sergeant Wargear": False,
#                                  "Weapons": {
#                                      "Melta Rifle": {"Type": "Assault", "Attacks": 2, "Range": 24, "Strength": 8,
#                                                      "AP": 4,
#                                                      "Damage": "D6"},
#                                      "Close Combat Weapon": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                              "Strength": "User",
#                                                              "AP": 0, "Damage": 1, "sWeapon": False,
#                                                              "Unwieldy": False}
#                                  }
#                                  },
#                   "Heavy Intercessor": {"M": 5, "WS": 3, "BS": 3, "S": 4, "T": 4, "W": 3, "A": 2, "Ld": 8, "Sv": 3,
#                                         "Size": 4,
#                                         "Faction": "Space Marines", "Sergeant": True, "Sergeant Wargear": False,
#                                         "Weapons": {
#                                             "Heavy Bolt Rifle": {"Type": "Rapid Fire", "Attacks": 1, "Range": 36,
#                                                                  "Strength": 5,
#                                                                  "AP": 1, "Damage": 1, "sWeapon": False},
#                                             "Heavy Bolter": {"Type": "Heavy", "Attacks": 3, "Range": 36,
#                                                              "Strength": 5, "AP": 1,
#                                                              "Damage": 2, "sWeapon": False},
#                                             "Close Combat Weapon": {"Type": "Melee", "Attacks": "User",
#                                                                     "Range": "Melee",
#                                                                     "Strength": "User", "AP": 0, "Damage": 1,
#                                                                     "sWeapon": False,
#                                                                     "Unwieldy": False},
#                                         }
#                                         },
#                   "Grey Knight": {"M": 6, "WS": 3, "BS": 3, "S": 4, "T": 4, "W": 1, "A": 1, "Ld": 7, "Sv": 3,
#                                   "Size": 4,
#                                   "Faction": "Grey Knights", "Sergeant": True, "Sergeant Wargear": False,
#                                   "Weapons": {
#                                       "Storm Bolter": {"Type": "Rapid Fire", "Attacks": 2, "Range": 24,
#                                                        "Strength": 4, "AP": 0,
#                                                        "Damage": 1, "sWeapon": False},
#                                       "Nemesis Force Sword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                               "Strength": "User", "AP": 3, "Damage": "D3",
#                                                               "sWeapon": False,
#                                                               "Unwieldy": False},
#                                       "Nemesis Force Halberd": {"Type": "Melee", "Attacks": "User",
#                                                                 "Range": "Melee",
#                                                                 "Strength": "1+", "AP": 2, "Damage": "D3",
#                                                                 "sWeapon": False,
#                                                                 "Unwieldy": False}}},
#                   "Retributor": {"M": 6, "WS": 4, "BS": 3, "S": 3, "T": 3, "W": 1, "A": 1, "Ld": 6, "Sv": 3,
#                                  "Size": 4,
#                                  "Faction": "Adepta Sororitas", "Sergeant": True, "Sergeant Wargear": True,
#                                  "Weapons": {
#                                      "Multi Melta": {"Type": "Heavy", "Attacks": 2, "Range": 24, "Strength": 8,
#                                                      "AP": 4,
#                                                      "Damage": "D6", "sWeapon": False},
#                                      "Heavy Flamer": {"Type": "Heavy", "Attacks": "D6", "Range": 12, "Strength": 5,
#                                                       "AP": 1,
#                                                       "Damage": 1, "sWeapon": False},
#                                      "Power Sword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                      "Strength": "1+",
#                                                      "AP": 3, "Damage": 1, "sWeapon": True, "Unwieldy": False},
#                                  }},
#
#                   "Skitarii Vanguard": {"M": 6, "WS": 4, "BS": 3, "S": 3, "T": 3, "W": 1, "A": 1, "Ld": 6, "Sv": 4,
#                                         "Size": 4,
#                                         "Faction": "Adeptus Mechanicus", "Sergeant": True, "Sergeant Wargear": True,
#                                         "Weapons": {
#                                             "Radium Carbine": {"Type": "Assault", "Attacks": 3, "Range": 18,
#                                                                "Strength": 3, "AP": 0,
#                                                                "Damage": 1, "sWeapon": False},
#                                             "Close Combat Weapon": {"Type": "Melee", "Attacks": "User",
#                                                                     "Range": "Melee",
#                                                                     "Strength": "User", "AP": 0, "Damage": 1,
#                                                                     "sWeapon": False,
#                                                                     "Unwieldy": False},
#                                             "Phosphor Blast Pistol": {"Type": "Pistol", "Attacks": 1, "Range": 12,
#                                                                       "Strength": 5,
#                                                                       "AP": 1, "Damage": 1, "sWeapon": True},
#                                             "Arc Pistol": {"Type": "Pistol", "Attacks": 1, "Range": 12,
#                                                            "Strength": 6, "AP": 1,
#                                                            "Damage": 1, "sWeapon": True},
#                                             "Arc Maul": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                          "Strength": "2+",
#                                                          "AP": 1, "Damage": 1, "sWeapon": True, "Unwieldy": False},
#                                             "Power Sword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                             "Strength": "1+",
#                                                             "AP": 3, "Damage": 1, "sWeapon": True,
#                                                             "Unwieldy": False},
#                                         }},
#                   "Skitarii Ranger": {"M": 6, "WS": 4, "BS": 3, "S": 3, "T": 3, "W": 1, "A": 1, "Ld": 6, "Sv": 4,
#                                       "Size": 4,
#                                       "Faction": "Adeptus Mechanicus", "Sergeant": True, "Sergeant Wargear": True,
#                                       "Weapons": {
#                                           "Galvanic Rifle": {"Type": "Rapid Fire", "Attacks": 1, "Range": 30,
#                                                              "Strength": 4, "AP": 0,
#                                                              "Damage": 1, "sWeapon": False},
#                                           "Close Combat Weapon": {"Type": "Melee", "Attacks": "User",
#                                                                   "Range": "Melee",
#                                                                   "Strength": "User", "AP": 0, "Damage": 1,
#                                                                   "sWeapon": False,
#                                                                   "Unwieldy": False},
#                                           "Phosphor Blast Pistol": {"Type": "Pistol", "Attacks": 1, "Range": 12,
#                                                                     "Strength": 5,
#                                                                     "AP": 1, "Damage": 1, "sWeapon": True},
#                                           "Arc Pistol": {"Type": "Pistol", "Attacks": 1, "Range": 12, "Strength": 6,
#                                                          "AP": 1,
#                                                          "Damage": 1, "sWeapon": True},
#                                           "Arc Maul": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                        "Strength": "2+",
#                                                        "AP": 1, "Damage": 1, "sWeapon": True, "Unwieldy": False},
#                                           "Power Sword": {"Type": "Melee", "Attacks": "User", "Range": "Melee",
#                                                           "Strength": "1+",
#                                                           "AP": 3, "Damage": 1, "sWeapon": True,
#                                                           "Unwieldy": False}}}

def hitRoll(unit, hit_roll_weapon, rapid_fire_valid, hitMods, movedValid, Sergeant):
    tempNumHits = 0
    if datasheets[unit]["Weapons"][weapon]["Attacks"] == "User":
        numAttacks = datasheets[unit]["A"]
        if Sergeant:
            numAttacks += 1
    elif datasheets[unit]["Weapons"][weapon]["Attacks"] == "D6":
        numAttacks = d6()
    else:
        numAttacks = datasheets[unit]["Weapons"][weapon]["Attacks"]
    if datasheets[unit]["Weapons"][weapon]["Type"] == "Melee":
        hitCheck = datasheets[unit]["WS"]
        if datasheets[unit]["Weapons"][weapon]["Unwieldy"]: hitCheck += 1
    elif datasheets[unit]["Weapons"][weapon]["Type"] == "Rapid Fire":
        if rapid_fire_valid == "y":
            numAttacks *= 2
        hitCheck = datasheets[unit]["BS"]
    elif movedValid == "y":
        hitCheck = datasheets[unit]["BS"] + 1
        hitMods += 1
    else:
        hitCheck = datasheets[unit]["BS"]
    if coverType == "h":
        hitCheck += 1
        hitMods += 1
    if hitMods > 1: hitCheck = datasheets[unit]["BS"] + 1
    if hitMods < -1: hitCheck = datasheets[unit]["BS"] - 1
    if weapon == "Heavy Flamer" or weapon == "Hand Flamer" or weapon == "Flamer":
        hitCheck = 1
    for i in range(numAttacks):
        hitroll = d6()
        if hitroll >= hitCheck:
            tempNumHits += 1
    return tempNumHits

def getHits(unit, weapon, sWeapon):
    numHits = 0
    hitMods = 0
    hitsDict = {weapon: {"Num Hits": 0}, sWeapon: {"Num Hits": 0}}
    if datasheets[unit]["Weapons"][weapon]["Type"] == "Rapid Fire":
        rapidFireValid = "y"  # input("Is the gun rapid firing (y/n): ")
        movedValid = "n"
    elif datasheets[unit]["Weapons"][weapon]["Type"] == "Heavy":
        movedValid = input("Did you move (y/n): ")
        rapidFireValid = "n"
    elif datasheets[unit]["Weapons"][weapon]["Type"] == "Assault":
        movedValid = input("Did you advance (y/n): ")
        rapidFireValid = "n"
    else:
        rapidFireValid = "n"
        movedValid = "n"
    for i in range(datasheets[unit]["Size"]):
        numHits += hitRoll(unit, weapon, rapidFireValid, hitMods, movedValid, False)
    hitsDict[weapon]["Num Hits"] = numHits
    if datasheets[unit]["Sergeant"]:
        if datasheets[unit]["Sergeant Wargear"]:
            if datasheets[unit]["Weapons"][weapon]["Type"] == "Melee":
                hitsDict[sWeapon]["Num Hits"] += hitRoll(unit, sWeapon, rapidFireValid, hitMods, movedValid, True)
            else:
                hitsDict[weapon]["Num Hits"] += hitRoll(unit, weapon, rapidFireValid, hitMods, movedValid, True)
    return hitsDict

def getWounds(woundWeapon, numHits):
    global modifier, s
    plague = False
    if datasheets[attacker]["Faction"] == "Deathguard":
        if datasheets[attacker]["Weapons"][woundWeapon]["Plague"]:
            plague = True
    if datasheets[attacker]["Weapons"][woundWeapon]["Strength"] == "User":
        s = datasheets[attacker]["S"]
    elif type(datasheets[attacker]["Weapons"][woundWeapon]["Strength"]) != int:
        for i in datasheets[attacker]["Weapons"][woundWeapon]["Strength"]:
            if i == "+":
                s = datasheets[attacker]["S"] + modifier
            elif i == "-":
                s = datasheets[attacker]["S"] - modifier
            elif i == "*":
                s = datasheets[attacker]["S"] * modifier
            elif i == "/":
                s = datasheets[attacker]["S"] / modifier
            else:
                modifier = int(i)
    else:
        s = datasheets[attacker]["Weapons"][woundWeapon]["Strength"]
    t = datasheets[defender]["T"]
    if datasheets[attacker] == "Skitarii Vanguard":
        if datasheets[attacker]["Weapons"][woundWeapon]["Type"] == "Melee":
            t -= 1
    if s / 2 >= t:
        woundCheck = 2
    elif s > t:
        woundCheck = 3
    elif s * 2 <= t:
        woundCheck = 6
    elif s < t:
        woundCheck = 5
    else:
        woundCheck = 4
    numWounds = 0
    rollList = []
    for i in range(numHits):
        woundRoll = d6()
        rollList.append(woundRoll)
        if plague:
            if woundRoll == 1:
                woundRoll = d6()
        if woundRoll >= woundCheck:
            numWounds += 1
    # print(woundWeapon, ": ", numWounds)
    return numWounds

def getSaves(saveWeapon, numWounds):
    saveCheck = datasheets[defender]["Sv"] + datasheets[attacker]["Weapons"][saveWeapon]["AP"]
    if coverType == "l" or coverType == "h":
        saveCheck -= 1
    fSaves = 0
    rollList = []
    if saveCheck == 1:
        saveCheck = 2
    for i in range(numWounds):
        saveRoll = d6()
        rollList.append(saveRoll)
        if saveRoll < saveCheck:
            fSaves += 1
    # print(rollList)
    # print("Amount failed: ",fSaves)
    return fSaves

def kills(tempWeapon, fSaves):
    kills = 0
    damage = 0
    wounds = datasheets[defender]["W"]
    if datasheets[attacker]["Weapons"][tempWeapon]["Damage"] == "D6":
        weaponDamage = d6()
    elif datasheets[attacker]["Weapons"][tempWeapon]["Damage"] == "D3":
        weaponDamage = d3()
    else:
        weaponDamage = datasheets[attacker]["Weapons"][tempWeapon]["Damage"]
    if tempWeapon == "Multi Melta" or tempWeapon == "Melta" or tempWeapon == "Inferno Pistol" or tempWeapon == "Melta Rifle":
        print("Are you in melta range (y/n)?")
        inMelta = input("In melta range: ")
        if inMelta == "y":
            weaponDamage = d6() + 2
        else:
            weaponDamage = d6()
    # print(weaponDamage)
    if datasheets[defender]["Faction"] == "Deathguard":
        if weaponDamage - 1 > 0:
            weaponDamage -= 1
    # print (weaponDamage)
    for i in range(fSaves):
        damage += weaponDamage
        if damage >= wounds:
            kills += 1
            damage = 0
        # print(kills, damage)
        # if kills == datasheets[defender]["Size"]:
        #     break
    tempKillsList = [kills, damage]
    # print(f"{kills} dead {defender}, {damage} wounds remaining")
    return tempKillsList

def getAttacker():
    # print("Choose a unit to attack with. Options: ")
    # for i in datasheets:
    #     print(f"   {i}")
    attacker = "Intercessor"  # input("Attacking unit: ")
    attackerValid = False
    for i in datasheets:
        if attacker == i:
            attackerValid = True
    return attacker, attackerValid

attackerList = getAttacker()
while not attackerList[1]:
    print(f"{attackerList[0]} is not an option. Please enter complete name of option. Please try again.")
    attackerList = getAttacker()
attacker = attackerList[0]

def getWeapon(attacker):
    # print("Choose a weapon to attack with. Options: ")
    for i in datasheets[attacker]["Weapons"]:
        if not datasheets[attacker]["Weapons"][i]["sWeapon"]:
            # print(f"   {i}")
            pass
    weapon = "Bolt Rifle"  # input("Attacking weapon: ")
    weaponValid = False
    for i in datasheets[attacker]["Weapons"]:
        if weapon == i:
            weaponValid = True
    return weapon, weaponValid

weaponList = getWeapon(attacker)
while not weaponList[1]:
    print(f"{weaponList[0]} is not an option. Please enter complete name of option. Please try again.")
    weaponList = getWeapon(attacker)
weapon = weaponList[0]

def getSWeapon(attacker):
    print("Choose weapon for the sergeant to attack with. Options: ")
    for i in datasheets[attacker]["Weapons"]:
        if datasheets[attacker]["Weapons"][i]["sWeapon"]:
            print(f"    {i}")
    sWeapon = input("Sergeant weapon: ")
    sWeaponValid = False
    for i in datasheets[attacker]["Weapons"]:
        if sWeapon == i:
            sWeaponValid = True
    return sWeapon, sWeaponValid

if datasheets[attacker]["Sergeant Wargear"]:
    if datasheets[attacker]["Weapons"][weapon]["Type"] == "Melee":
        sWeaponValid = input("Does the sergeant have its own weapon (y/n): ")
        if sWeaponValid == "y":
            sWeaponList = getSWeapon(attacker)
            while not sWeaponList[1]:
                print(f"{sWeaponList[0]} is not an option. Please enter complete name of option. Please try again.")
                sWeaponList = getSWeapon(attacker)
            sWeapon = sWeaponList[0]
        else:
            sWeapon = weapon
    else:
        sWeapon = weapon
        sWeaponValid = "n"

def getDefender():
    # print("Choose a unit to attack against. Options: ")
    # for i in datasheets:
    #     print(f"   {i}")
    defender = "Guardsmen"  # input("Attacking at: ")
    defenderValid = False
    for i in datasheets:
        if defender == i:
            defenderValid = True
    return defender, defenderValid

defenderList = getDefender()
while not defenderList[1]:
    print(f"{defenderList[0]} is not an option. Please enter complete name of option. Please try again.")
    defenderList = getDefender()
defender = defenderList[0]

def getCover():
    coverOptions = ["none", "light", "heavy"]
    coverType = "none"  # input("Is there any cover (none, light, or heavy): ")
    coverValid = False
    for i in coverOptions:
        if coverType == i:
            coverValid = True
    return coverType, coverValid

if datasheets[attacker]["Weapons"][weapon]["Type"] == "Melee":
    coverType = "n"
else:
    coverList = getCover()
    while not coverList[1]:
        print(f"{coverList[0]} is not an option. Please enter complete name of option. Please try again.")
        coverList = getCover()
    coverType = coverList[0]

def run_sim(attacker, weapon, sWeapon, defender, coverType):
    woundDict = {weapon: {"Num Wounds": 0}, sWeapon: {"Num Wounds": 0}}
    saveDict = {weapon: {"Num fSaves": 0}, sWeapon: {"Num fSaves": 0}}
    hitsDict = getHits(attacker, weapon, sWeapon)
    for i in hitsDict:
        woundDict[i]["Num Wounds"] += getWounds(i, hitsDict[i]["Num Hits"])
    for i in woundDict:
        saveDict[i]["Num fSaves"] += getSaves(i, woundDict[i]["Num Wounds"])
    killsList = []
    for i in saveDict:
        killsList += kills(i, saveDict[i]["Num fSaves"])
    deaths = killsList[0]
    wounds = killsList[1]
    if sWeaponValid == "y":
        deaths += killsList[2]
        wounds += killsList[3]
    if wounds >= datasheets[defender]["W"]:
        deaths += 1
        wounds = 0
    # if deaths == 1:
    #     if wounds == 0:
    #         print(f"You killed {deaths} {defender}.\n")
    #     else:
    #         print(f"You killed {deaths} {defender}. One {defender} has taken another {wounds} wounds.\n")
    # else:
    #     if wounds == 0:
    #         print(f"You killed {deaths} {defender}s.\n")
    #     else:
    #         print(f"You killed {deaths} {defender}s. One {defender} has taken another {wounds} wounds.\n")
    deaths_list.append(deaths)
    wound_list.append(wounds)

num_of_trials = 10000
for i in range(num_of_trials):
    run_sim(attacker, weapon, sWeapon, defender, coverType)
print(f"Average number of deaths: {sum(deaths_list) / len(deaths_list)} ")
deaths_list = []
defender = "Intercessor"
for i in range(num_of_trials):
    run_sim(attacker, weapon, sWeapon, defender, coverType)
print(f"Average number of deaths: {sum(deaths_list) / len(deaths_list)} ")
deaths_list = []
defender = "Plague Marine"
for i in range(num_of_trials):
    run_sim(attacker, weapon, sWeapon, defender, coverType)
print(f"Average number of deaths: {sum(deaths_list) / len(deaths_list)} ")
deaths_list = []
