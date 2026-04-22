def start(troops):
    for unit in troops:
        if unit.name is None:
            continue
        # Castle
        elif unit.name == "Pikeman":
            unit.speed = 4
        elif unit.name == "Halberdier":
            unit.speed = 5
        elif unit.name == "Archer":
            unit.speed = 4
        elif unit.name == "Marksman":
            unit.speed = 6
        elif unit.name == "Griffin":
            unit.speed = 6
        elif unit.name == "Royal_griffin":
            unit.speed = 9
        elif unit.name == "Swordsman":
            unit.speed = 5
        elif unit.name == "Crusader":
            unit.speed = 6
        elif unit.name == "Monk":
            unit.speed = 5
        elif unit.name == "Zealot":
            unit.speed = 7
        elif unit.name == "Cavalier":
            unit.speed = 7
        elif unit.name == "Champion":
            unit.speed = 9
        elif unit.name == "Angel":
            unit.speed = 12
        elif unit.name == "Archangel":
            unit.speed = 18
        # Inferno
        elif unit.name == "Imp":
            unit.speed = 5
        elif unit.name == "Familiar":
            unit.speed = 7
        elif unit.name == "Gog":
            unit.speed = 4
        elif unit.name == "Magog":
            unit.speed = 6
        elif unit.name == "Hell_hound":
            unit.speed = 7
        elif unit.name == "Cerberus":
            unit.speed = 8
        elif unit.name == "Demon":
            unit.speed = 5
        elif unit.name == "Horned_demon":
            unit.speed = 6
        elif unit.name == "Pit_fiend":
            unit.speed = 6
        elif unit.name == "Pit_lord":
            unit.speed = 7
        elif unit.name == "Efreet":
            unit.speed = 9
        elif unit.name == "Efreet_sultan":
            unit.speed = 14
        elif unit.name == "Devil":
            unit.speed = 11
        elif unit.name == "Archdevil":
            unit.speed = 17