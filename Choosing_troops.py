import pygame, sys

pygame.init()

troops = []
is_continue = False

selection_panel_click = None
selection_panel = pygame.image.load("image/selection_panel.png")
choice_selection_panel = pygame.image.load("image/Choise_selection_panel.png")
click_selection_panel = pygame.image.load("image/Click_selection_panel.png")
background_quantity = pygame.image.load("image/background_quantity.png")
choice_selection_panel.set_colorkey((255,255,255))
click_selection_panel.set_colorkey((255,255,255))

current_unit = None
current_city = None
choice = pygame.image.load("image/Choosing_location/choice.png")
choice_list = pygame.image.load("image/Choosing_location/choice_list.png")
choice_list.set_colorkey((255,255,255))
choice.set_colorkey((255,255,255))

font = pygame.font.Font("font/timesnewromanpsmt.ttf", 30)
font2 = pygame.font.Font("font/timesnewromanpsmt.ttf", 15)
text_plater1 = font.render("Player 1", True, (244, 244, 244))
text_plater2 = font.render("Player 2", True, (244, 244, 244))

text_quantity = font.render("Количество:", True, (244, 244, 244))

def start_selecting_troops(display):
    global selection_panel_click
    global current_city
    global current_unit
    while not is_continue:
        renderer(display)

        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()


        for ar in army:
            ar.image_render(display)
            if ar.rect.collidepoint(mouse):
                ar.choice_render(display)
                if mouse_button(events):
                    if selection_panel_click == ar:
                        selection_panel_click = None
                    else:
                        selection_panel_click = ar

        if current_city is None:
            for c in cities:
                c.blit_img(display)
                if c.rect.collidepoint(mouse):
                    c.choice_render(display)
                    if mouse_button(events):
                        current_city = c
        else:
            for arm in current_city.army_list:
                if arm.rect.collidepoint(mouse):
                    arm.choice_render(display)
                    if mouse_button(events):
                        current_unit = arm
                        arm.click()

        if go_continue.rect.collidepoint(mouse):
            go_continue.choice_render(display)
            if mouse_button(events):
                go_continue.click()

        if selection_panel_click is not None:
            selection_panel_click.quantity = quantity.numbers
            selection_panel_click.click_render(display)

        quantity.click_button(events)

        for event in events:  # обработка закрытия окна
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

    return troops

def mouse_button(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True

def renderer(display):
    display.fill((0, 0, 0))
    display.blit(text_plater1, (5, 0))
    display.blit(selection_panel, (5, 40))
    display.blit(text_plater2, (5, 120))
    display.blit(selection_panel, (5, 160))

    display.blit(text_quantity, (300, 250))
    quantity.image_render(display)
    quantity.numbers_render(display)

    go_continue.text_render(display)

    if current_unit is not None and current_unit.back == False:
        display.blit(current_unit.unit_characteristics, (10, 250))
        if current_unit.feature is not None:
            display.blit(font2.render(current_unit.feature, True, (244, 244, 244)),(10,412))

    if current_city is not None:
        current_city.blit_army_list(display)

    # if selection_panel_click is not None:
    #     selection_panel_click.click_render(display)

class PlayersArmy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = None
        self.image = None
        self.rect = pygame.Rect(self.x, self.y, 62, 68)
        self.quantity = "0"
    def choice_render(self, display):
        display.blit(choice_selection_panel,(self.x,self.y))
    def click_render(self, display):
        display.blit(click_selection_panel,(self.x,self.y))
    def image_render(self, display):
        if self.image is not None:
            display.blit(self.image,(self.x,self.y))
            display.blit(background_quantity,(self.x,self.y + 53))
            display.blit(font2.render(self.quantity, True, (244, 244, 244)), (self.x + 3,self.y + 50))

class City:
    def __init__(self, x, y, img, img_list, army_list):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 60, 66)
        self.img = img
        self.img_list = img_list
        self.army_list = army_list
    def choice_render(self, display):
        display.blit(choice,(self.x,self.y))
    def blit_img(self,display):
        display.blit(self.img, (self.x, self.y))
    def blit_army_list(self, display):
        display.blit(self.img_list, (500, 20))

class ArmyList:
    def __init__(self, x, y, unit_characteristics = None, image = None, name = None, feature = None, back = False):
        self.x = x
        self.y = y
        self.unit_characteristics = unit_characteristics
        self.image = image
        self.name = name
        self.feature = feature
        self.back = back
        self.rect = pygame.Rect(self.x, self.y, 300, 32)
    def choice_render(self, display):
        display.blit(choice_list,(self.x,self.y))
    def click(self):
        global current_city
        if self.back:
            current_city = None
        else:
            if selection_panel_click is not None:
                selection_panel_click.image = self.image
                selection_panel_click.name = self.name

class Quantity:
    def __init__(self, img_quantity):
        self.x = 300
        self.y = 280
        self.img_quantity = img_quantity
        self.rect = pygame.Rect(self.x, self.y, 180, 30)
        self.numbers = "1"
    def image_render(self, display):
        display.blit(self.img_quantity, (self.x,self.y))
    def numbers_render(self, display):
        display.blit(font.render(self.numbers, True, (0,0,0)), (self.x,self.y))
    def click_button(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "1"
                if event.key == pygame.K_2:
                    if self.numbers == "1":
                        self.numbers = "2"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "2"
                if event.key == pygame.K_3:
                    if self.numbers == "1":
                        self.numbers = "3"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "3"
                if event.key == pygame.K_4:
                    if self.numbers == "1":
                        self.numbers = "4"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "4"
                if event.key == pygame.K_5:
                    if self.numbers == "1":
                        self.numbers = "5"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "5"
                if event.key == pygame.K_6:
                    if self.numbers == "1":
                        self.numbers = "6"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "6"
                if event.key == pygame.K_7:
                    if self.numbers == "1":
                        self.numbers = "7"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "7"
                if event.key == pygame.K_8:
                    if self.numbers == "1":
                        self.numbers = "8"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "8"
                if event.key == pygame.K_9:
                    if self.numbers == "1":
                        self.numbers = "9"
                    elif len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "9"
                if event.key == pygame.K_0:
                    if len(self.numbers) == 4:
                        return
                    else:
                        self.numbers = self.numbers + "0"
                if event.key == pygame.K_BACKSPACE:
                    if len(self.numbers) == 1:
                        self.numbers = "1"
                    else:
                        self.numbers = self.numbers[:-1]


class Continue:
    def __init__(self, text, img_choice):
        self.x = 630
        self.y = 560
        self.text = text
        self.img_choice = img_choice
        self.img_choice.set_colorkey((255,255,255))
        self.rect = pygame.Rect(self.x,self.y,170,40)
    def text_render(self, display):
        display.blit(self.text,(self.x + 5,self.y))
    def choice_render(self,display):
        display.blit(self.img_choice,(self.x,self.y))
    def click(self):
        global is_continue
        for ar in army:
            troops.append((ar.name,ar.quantity))
            is_continue = True

army = [PlayersArmy(10, 46), PlayersArmy(75, 46), PlayersArmy(140, 46), PlayersArmy(206, 46), PlayersArmy(272, 46), PlayersArmy(338, 46), PlayersArmy(405, 46),
        PlayersArmy(10, 165), PlayersArmy(75, 165), PlayersArmy(140, 165), PlayersArmy(206, 165), PlayersArmy(272, 165), PlayersArmy(338, 165), PlayersArmy(405, 165)]

castle_army = [ArmyList(500, 20, pygame.image.load("image/unit_characteristics/Castle/Pikeman.png"), pygame.image.load("image/icon_units/Castle/Pikeman.png"), "Pikeman"),
               ArmyList(500, 51, pygame.image.load("image/unit_characteristics/Castle/Halberdier.png"), pygame.image.load("image/icon_units/Castle/Halberdier.png"), "Halberdier"),
               ArmyList(500, 82, pygame.image.load("image/unit_characteristics/Castle/Archer.png"), pygame.image.load("image/icon_units/Castle/Archer.png"), "Archer"),
               ArmyList(500, 113, pygame.image.load("image/unit_characteristics/Castle/Marksman.png"), pygame.image.load("image/icon_units/Castle/Marksman.png"),"Marksman" , "Два выстрела"),
               ArmyList(500, 144, pygame.image.load("image/unit_characteristics/Castle/Griffin.png"), pygame.image.load("image/icon_units/Castle/Griffin.png"),"Griffin", "Отвечает дважды"),
               ArmyList(500, 175, pygame.image.load("image/unit_characteristics/Castle/Royal_griffin.png"), pygame.image.load("image/icon_units/Castle/Royal_griffin.png"),"Royal_griffin", "Отвечает всем"),
               ArmyList(500, 206, pygame.image.load("image/unit_characteristics/Castle/Swordsman.png"), pygame.image.load("image/icon_units/Castle/Swordsman.png"), "Swordsman"),
               ArmyList(500, 237, pygame.image.load("image/unit_characteristics/Castle/Crusader.png"), pygame.image.load("image/icon_units/Castle/Crusader.png"),"Crusader", "Атакует дважды"),
               ArmyList(500, 268, pygame.image.load("image/unit_characteristics/Castle/Monk.png"), pygame.image.load("image/icon_units/Castle/Monk.png"), "Monk"),
               ArmyList(500, 299, pygame.image.load("image/unit_characteristics/Castle/Zealot.png"), pygame.image.load("image/icon_units/Castle/Zealot.png"), "Zealot", "Нет штрафа ближнего боя"),
               ArmyList(500, 330, pygame.image.load("image/unit_characteristics/Castle/Cavalier.png"), pygame.image.load("image/icon_units/Castle/Cavalier.png"),"Cavalier", "Турнирное преимущество"),
               ArmyList(500, 361, pygame.image.load("image/unit_characteristics/Castle/Champion.png"), pygame.image.load("image/icon_units/Castle/Champion.png"),"Champion", "Турнирное преимущество"),
               ArmyList(500, 392, pygame.image.load("image/unit_characteristics/Castle/Angel.png"), pygame.image.load("image/icon_units/Castle/Angel.png"),"Angel", "Ненависть к дьяволам"),
               ArmyList(500, 423, pygame.image.load("image/unit_characteristics/Castle/Archangel.png"), pygame.image.load("image/icon_units/Castle/Archangel.png"),"Archangel", "+1 к морали, ненависть к дьяволам, воскрешение"),
               ArmyList(500, 454, back = True)]

inferno_army = [ArmyList(500, 20, pygame.image.load("image/unit_characteristics/inferno/Imp.png"), pygame.image.load("image/icon_units/Inferno/Imp.png"), "Imp"),
               ArmyList(500, 51, pygame.image.load("image/unit_characteristics/inferno/Familiar.png"), pygame.image.load("image/icon_units/Inferno/Familiar.png"),"Familiar", "Кража магии"),
               ArmyList(500, 82, pygame.image.load("image/unit_characteristics/inferno/Gog.png"), pygame.image.load("image/icon_units/Inferno/Gog.png"), "Gog"),
               ArmyList(500, 113, pygame.image.load("image/unit_characteristics/inferno/Magog.png"), pygame.image.load("image/icon_units/Inferno/Magog.png"),"Magog", "Метает огненный шар"),
               ArmyList(500, 144, pygame.image.load("image/unit_characteristics/inferno/Hell_hound.png"), pygame.image.load("image/icon_units/Inferno/Hell_hound.png"), "Hell_hound"),
               ArmyList(500, 175, pygame.image.load("image/unit_characteristics/inferno/Cerberus.png"), pygame.image.load("image/icon_units/Inferno/Cerberus.png"), "Cerberus", "Трёхглавая атака, враг не отвечает"),
               ArmyList(500, 206, pygame.image.load("image/unit_characteristics/inferno/Demon.png"), pygame.image.load("image/icon_units/Inferno/Demon.png"), "Demon"),
               ArmyList(500, 237, pygame.image.load("image/unit_characteristics/inferno/Horned_demon.png"), pygame.image.load("image/icon_units/Inferno/Horned_demon.png"), "Horned_demon"),
               ArmyList(500, 268, pygame.image.load("image/unit_characteristics/inferno/Pit_fiend.png"), pygame.image.load("image/icon_units/Inferno/Pit_fiend.png"), "Pit_fiend"),
               ArmyList(500, 299, pygame.image.load("image/unit_characteristics/inferno/Pit_lord.png"), pygame.image.load("image/icon_units/Inferno/Pit_lord.png"),"Pit_lord", "Поднимает демонов из тел павших союзников"),
               ArmyList(500, 330, pygame.image.load("image/unit_characteristics/inferno/Efreet.png"), pygame.image.load("image/icon_units/Inferno/Efreet.png"),"Efreet", "Иммунитет к огню, ненависть к джиннам"),
               ArmyList(500, 361, pygame.image.load("image/unit_characteristics/inferno/Efreet_sultan.png"), pygame.image.load("image/icon_units/Inferno/Efreet_sultan.png"),"Efreet_sultan", "Огненный щит, иммунитет к огню, ненависть к джиннам"),
               ArmyList(500, 392, pygame.image.load("image/unit_characteristics/inferno/Devil.png"), pygame.image.load("image/icon_units/Inferno/Devil.png"),"Devil", "-1 к удаче противника, враг не отвечает, ненависть к ангелам"),
               ArmyList(500, 423, pygame.image.load("image/unit_characteristics/inferno/Arch_devil.png"), pygame.image.load("image/icon_units/Inferno/Arch_devil.png"),"Arch_devil", "-1 к удаче противника, враг не отвечает, ненависть к ангелам"),
               ArmyList(500, 454, back = True)]

cities = [City(500, 20, pygame.image.load("image/Choosing_location/Castle.png"), pygame.image.load("image/Choosing_location/Castle_list.png"), castle_army),
          City(570, 20, pygame.image.load("image/Choosing_location/Inferno.png"), pygame.image.load("image/Choosing_location/Inferno_list.png"), inferno_army)]

quantity = Quantity(pygame.image.load("image/quantity/quantity.png"))
go_continue = Continue(font.render("Продолжить", True, (244, 244, 244)), pygame.image.load("image/continue_choice.png"))