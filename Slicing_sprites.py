import pygame

# в этом классе и далее "x" и "y" отвечают за смещение, что бы картинка легла не в левый верхний угол клетки, а правильно, относительно ног юнита
class Stand:
    def __init__(self, x, y, render):
        self.x = x
        self.y = y
        self.render = render

def start(troops):
    for unit in troops:
        if unit.name is None:
            continue
        # Castle
        elif unit.name == "Pikeman":
            pikeman_sprite = pygame.image.load("image/Units/sprites/Castle/Pikeman.png")
            if unit.is_player2:
                unit.stand = Stand(-10, -60, pygame.transform.flip(pikeman_sprite.subsurface(pygame.Rect(9, 16, 48, 95)), True, False))
            else:
                unit.stand = Stand(5, -60, pikeman_sprite.subsurface(pygame.Rect(9, 16, 48, 95)))
        elif unit.name == "Halberdier":
            halberdier_sprite = pygame.image.load("image/Units/sprites/Castle/Halberdier.png")
            if unit.is_player2:
                unit.stand = Stand(-10, -65, pygame.transform.flip(halberdier_sprite.subsurface(pygame.Rect(18,14,45,101)), True, False))
            else:
                unit.stand = Stand(5,-65,halberdier_sprite.subsurface(pygame.Rect(18,14,45,101)))
        elif unit.name == "Archer":
            archer_sprite = pygame.image.load("image/Units/sprites/Castle/Archer.png")
            if unit.is_player2:
                unit.stand = Stand(0, -40, pygame.transform.flip(archer_sprite.subsurface(pygame.Rect(13, 8, 40, 76)), True, False))
            else:
                unit.stand = Stand(0, -40, archer_sprite.subsurface(pygame.Rect(13, 8, 40, 76)))
        elif unit.name == "Marksman":
            marksman_sprite = pygame.image.load("image/Units/sprites/Castle/Marksman.png")
            if unit.is_player2:
                unit.stand = Stand(0, -40, pygame.transform.flip(marksman_sprite.subsurface(pygame.Rect(6, 11, 39, 76)), True, False))
            else:
                unit.stand = Stand(0, -40, marksman_sprite.subsurface(pygame.Rect(6, 11, 39, 76)))
        elif unit.name == "Griffin":
            unit.is_two_cell = True
            griffin_sprite = pygame.image.load("image/Units/sprites/Castle/Griffin.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -55, pygame.transform.flip(griffin_sprite.subsurface(pygame.Rect(60, 29, 76, 90)), True, False))
            else:
                unit.stand = Stand(-35, -55, griffin_sprite.subsurface(pygame.Rect(60, 29, 76, 90)))
        elif unit.name == "Royal_griffin":
            unit.is_two_cell = True
            royal_griffin_sprite = pygame.image.load("image/Units/sprites/Castle/Royal_griffin.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -60, pygame.transform.flip(royal_griffin_sprite.subsurface(pygame.Rect(53, 11, 82, 100)), True, False))
            else:
                unit.stand = Stand(-40, -60, royal_griffin_sprite.subsurface(pygame.Rect(53, 11, 82, 100)))
        elif unit.name == "Swordsman":
            swordsman_sprite = pygame.image.load("image/Units/sprites/Castle/Swordsman.png")
            if unit.is_player2:
                unit.stand = Stand(0, -50, pygame.transform.flip(swordsman_sprite.subsurface(pygame.Rect(10, 41, 39, 84)), True, False))
            else:
                unit.stand = Stand(0,-50, swordsman_sprite.subsurface(pygame.Rect(10, 41, 39, 84)))
        elif unit.name == "Crusader":
            crusader_sprite = pygame.image.load("image/Units/sprites/Castle/Crusader.png")
            if unit.is_player2:
                unit.stand = Stand(0, -55, pygame.transform.flip(crusader_sprite.subsurface(pygame.Rect(15, 23, 41, 88)), True, False))
            else:
                unit.stand = Stand(0,-55, crusader_sprite.subsurface(pygame.Rect(15, 23, 41, 88)))
        elif unit.name == "Monk":
            monk_sprite = pygame.image.load("image/Units/sprites/Castle/Monk.png")
            if unit.is_player2:
                unit.stand = Stand(5, -45, pygame.transform.flip(monk_sprite.subsurface(pygame.Rect(16, 14, 33, 78)), True, False))
            else:
                unit.stand = Stand(5,-45, monk_sprite.subsurface(pygame.Rect(16, 14, 33, 78)))
        elif unit.name == "Zealot":
            zealot_sprite = pygame.image.load("image/Units/sprites/Castle/Zealot.png")
            if unit.is_player2:
                unit.stand = Stand(0, -45, pygame.transform.flip(zealot_sprite.subsurface(pygame.Rect(20, 6, 37, 80)), True, False))
            else:
                unit.stand = Stand(5,-45, zealot_sprite.subsurface(pygame.Rect(20, 6, 37, 80)))
        elif unit.name == "Cavalier":
            unit.is_two_cell = True
            cavalier_sprite = pygame.image.load("image/Units/sprites/Castle/Cavalier.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -70, pygame.transform.flip(cavalier_sprite.subsurface(pygame.Rect(4, 6, 93, 104)), True, False))
            else:
                unit.stand = Stand(-45,-70, cavalier_sprite.subsurface(pygame.Rect(4, 6, 93, 104)))
        elif unit.name == "Champion":
            unit.is_two_cell = True
            champion_sprite = pygame.image.load("image/Units/sprites/Castle/Champion.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -70, pygame.transform.flip(champion_sprite.subsurface(pygame.Rect(12, 10, 93, 104)), True, False))
            else:
                unit.stand = Stand(-45,-70, champion_sprite.subsurface(pygame.Rect(12, 10, 93, 104)))
        elif unit.name == "Angel":
            angel_sprite = pygame.image.load("image/Units/sprites/Castle/Angel.png")
            if unit.is_player2:
                unit.stand = Stand(0, -60, pygame.transform.flip(angel_sprite.subsurface(pygame.Rect(29, 7, 45, 96)), True, False))
            else:
                unit.stand = Stand(0,-60, angel_sprite.subsurface(pygame.Rect(29, 7, 45, 96)))
        elif unit.name == "Archangel":
            unit.is_two_cell = True
            archangel_sprite = pygame.image.load("image/Units/sprites/Castle/Archangel.png")
            if unit.is_player2:
                unit.stand = Stand(5, -65, pygame.transform.flip(archangel_sprite.subsurface(pygame.Rect(15, 30, 72, 104)), True, False))
            else:
                unit.stand = Stand(-35,-65, archangel_sprite.subsurface(pygame.Rect(15, 30, 72, 104)))
        # Inferno
        elif unit.name == "Imp":
            imp_sprite = pygame.image.load("image/Units/sprites/Inferno/Imp.png")
            if unit.is_player2:
                unit.stand = Stand(0, -30, pygame.transform.flip(imp_sprite.subsurface(pygame.Rect(36, 12, 41, 64)), True, False))
            else:
                unit.stand = Stand(0,-30, imp_sprite.subsurface(pygame.Rect(36, 12, 41, 64)))
        elif unit.name == "Familiar":
            familiar_sprite = pygame.image.load("image/Units/sprites/Inferno/Familiar.png")
            if unit.is_player2:
                unit.stand = Stand(0, -30, pygame.transform.flip(familiar_sprite.subsurface(pygame.Rect(37, 11, 42, 68)), True, False))
            else:
                unit.stand = Stand(0,-30, familiar_sprite.subsurface(pygame.Rect(37, 11, 42, 68)))
        elif unit.name == "Gog":
            gog_sprite = pygame.image.load("image/Units/sprites/Inferno/Gog.png")
            if unit.is_player2:
                unit.stand = Stand(0, -45, pygame.transform.flip(gog_sprite.subsurface(pygame.Rect(37, 20, 43, 79)), True, False))
            else:
                unit.stand = Stand(0,-45, gog_sprite.subsurface(pygame.Rect(37, 20, 43, 79)))
        elif unit.name == "Magog":
            magog_sprite = pygame.image.load("image/Units/sprites/Inferno/Magog.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -50, pygame.transform.flip(magog_sprite.subsurface(pygame.Rect(32, 21, 47, 84)), True, False))
            else:
                unit.stand = Stand(-5,-50, magog_sprite.subsurface(pygame.Rect(32, 21, 47, 84)))
        elif unit.name == "Hell_hound":
            unit.is_two_cell = True
            hell_hound_sprite = pygame.image.load("image/Units/sprites/Inferno/Hell_hound.png")
            if unit.is_player2:
                unit.stand = Stand(-10, -30, pygame.transform.flip(hell_hound_sprite.subsurface(pygame.Rect(34, 27, 86, 63)), True, False))
            else:
                unit.stand = Stand(-40,-30, hell_hound_sprite.subsurface(pygame.Rect(34, 27, 86, 63)))
        elif unit.name == "Cerberus":
            unit.is_two_cell = True
            cerberus_sprite = pygame.image.load("image/Units/sprites/Inferno/Cerberus.png")
            if unit.is_player2:
                unit.stand = Stand(-10, -35, pygame.transform.flip(cerberus_sprite.subsurface(pygame.Rect(17, 27, 89, 71)), True, False))
            else:
                unit.stand = Stand(-40,-35, cerberus_sprite.subsurface(pygame.Rect(17, 27, 89, 71)))
        elif unit.name == "Demon":
            demon_sprite = pygame.image.load("image/Units/sprites/Inferno/Demon.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -60, pygame.transform.flip(demon_sprite.subsurface(pygame.Rect(44, 11, 45, 97)), True, False))
            else:
                unit.stand = Stand(0,-60, demon_sprite.subsurface(pygame.Rect(44, 11, 45, 97)))
        elif unit.name == "Horned_demon":
            horned_demon_sprite = pygame.image.load("image/Units/sprites/Inferno/Horned_demon.png")
            if unit.is_player2:
                unit.stand = Stand(-5, -65, pygame.transform.flip(horned_demon_sprite.subsurface(pygame.Rect(32, 13, 47, 99)), True, False))
            else:
                unit.stand = Stand(0,-65, horned_demon_sprite.subsurface(pygame.Rect(32, 13, 47, 99)))
        elif unit.name == "Pit_fiend":
            pit_fiend_sprite = pygame.image.load("image/Units/sprites/Inferno/Pit_fiend.png")
            if unit.is_player2:
                unit.stand = Stand(0, -60, pygame.transform.flip(pit_fiend_sprite.subsurface(pygame.Rect(37, 11, 40, 95)), True, False))
            else:
                unit.stand = Stand(0,-60, pit_fiend_sprite.subsurface(pygame.Rect(37, 11, 40, 95)))
        elif unit.name == "Pit_lord":
            pit_lord_sprite = pygame.image.load("image/Units/sprites/Inferno/Pit_lord.png")
            if unit.is_player2:
                unit.stand = Stand(0, -60, pygame.transform.flip(pit_lord_sprite.subsurface(pygame.Rect(27, 11, 40, 94)), True, False))
            else:
                unit.stand = Stand(0,-60, pit_lord_sprite.subsurface(pygame.Rect(27, 11, 40, 94)))
        elif unit.name == "Efreet":
            efreet_sprite = pygame.image.load("image/Units/sprites/Inferno/Efreet.png")
            if unit.is_player2:
                unit.stand = Stand(5, -55, pygame.transform.flip(efreet_sprite.subsurface(pygame.Rect(19, 16, 37, 88)), True, False))
            else:
                unit.stand = Stand(0,-55, efreet_sprite.subsurface(pygame.Rect(19, 16, 37, 88)))
        elif unit.name == "Efreet_sultan":
            efreet_sultan_sprite = pygame.image.load("image/Units/sprites/Inferno/Efreet_sultan.png")
            if unit.is_player2:
                unit.stand = Stand(5, -55, pygame.transform.flip(efreet_sultan_sprite.subsurface(pygame.Rect(19, 8, 37, 91)), True, False))
            else:
                unit.stand = Stand(0,-55, efreet_sultan_sprite.subsurface(pygame.Rect(19, 8, 37, 91)))
        elif unit.name == "Devil":
            devil_sprite = pygame.image.load("image/Units/sprites/Inferno/Devil.png")
            if unit.is_player2:
                unit.stand = Stand(0, -70, pygame.transform.flip(devil_sprite.subsurface(pygame.Rect(31, 9, 43, 110)), True, False))
            else:
                unit.stand = Stand(0,-70, devil_sprite.subsurface(pygame.Rect(31, 9, 43, 110)))
        elif unit.name == "Archdevil":
            archdevil_sprite = pygame.image.load("image/Units/sprites/Inferno/Archdevil.png")
            if unit.is_player2:
                unit.stand = Stand(0, -80, pygame.transform.flip(archdevil_sprite.subsurface(pygame.Rect(570, 15, 43, 117)), True, False))
            else:
                unit.stand = Stand(0,-80, archdevil_sprite.subsurface(pygame.Rect(570, 15, 43, 117)))