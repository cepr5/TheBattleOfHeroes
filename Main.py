import pygame, sys
import Choosing_troops
import Slicing_sprites
import Characteristic_unit

display = pygame.display.set_mode((800,600))
background = pygame.image.load("image/Backgrounds/CmBkGrMt.png").convert_alpha()
panel = pygame.image.load("image/Panel.png").convert_alpha()
grid = pygame.image.load("image/grid.png").convert_alpha()
grid.set_colorkey((255,255,255))

mouse_cursor = pygame.image.load("image/MouseCursors.png").convert_alpha()
mouse_cursor_rect = pygame.Rect(8,9,17,18)
mouse_cursor = mouse_cursor.subsurface(mouse_cursor_rect)
mouse_cursor = pygame.transform.scale(mouse_cursor,(32,32))
mouse_cursor.set_colorkey((0,255,255))
cursor = pygame.cursors.Cursor((0,0),mouse_cursor.convert_alpha())
pygame.mouse.set_cursor(cursor)

current_unit = None
id_current_unit = 1

# Клетки карты
class Map:
    def __init__(self,x=0,y=0,is_edge=False):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,40,39)
        self.mouse_black = pygame.image.load("image/mouse_black.png").convert_alpha()
        self.mouse_black.set_alpha(100)
        self.current_unit = pygame.image.load("image/current_unit.png").convert()
        self.current_unit.set_colorkey((255, 255, 255))
        self.unit = None
    def render_mouse_black(self):
        display.blit(self.mouse_black,(self.x,self.y))
    def render_current_unit(self):
        if self.unit == current_unit:
            display.blit(self.current_unit,(self.x,self.y))

map = [[Map(94,102), Map(136,102), Map(178,102), Map(220,102), Map(262,102), Map(304,102), Map(346,102), Map(388,102), Map(430,102), Map(472,102), Map(514,102), Map(556,102), Map(598,102), Map(640,102), Map(682,102)],
       [Map(72,143), Map(114,143), Map(156,143), Map(198,143), Map(240,143), Map(282,143), Map(324,143), Map(366,143), Map(408,143), Map(450,143), Map(492,143), Map(534,143), Map(576,143), Map(618,143), Map(660,143)],
       [Map(94,184), Map(136,184), Map(178,184), Map(220,184), Map(262,184), Map(304,184), Map(346,184), Map(388,184), Map(430,184), Map(472,184), Map(514,184), Map(556,184), Map(598,184), Map(640,184), Map(682,184)],
       [Map(72,225), Map(114,225), Map(156,225), Map(198,225), Map(240,225), Map(282,225), Map(324,225), Map(366,225), Map(408,225), Map(450,225), Map(492,225), Map(534,225), Map(576,225), Map(618,225), Map(660,225)],
       [Map(94,266), Map(136,266), Map(178,266), Map(220,266), Map(262,266), Map(304,266), Map(346,266), Map(388,266), Map(430,266), Map(472,266), Map(514,266), Map(556,266), Map(598,266), Map(640,266), Map(682,266)],
       [Map(72,307), Map(114,307), Map(156,307), Map(198,307), Map(240,307), Map(282,307), Map(324,307), Map(366,307), Map(408,307), Map(450,307), Map(492,307), Map(534,307), Map(576,307), Map(618,307), Map(660,307)],
       [Map(94,348), Map(136,348), Map(178,348), Map(220,348), Map(262,348), Map(304,348), Map(346,348), Map(388,348), Map(430,348), Map(472,348), Map(514,348), Map(556,348), Map(598,348), Map(640,348), Map(682,348)],
       [Map(72,389), Map(114,389), Map(156,389), Map(198,389), Map(240,389), Map(282,389), Map(324,389), Map(366,389), Map(408,389), Map(450,389), Map(492,389), Map(534,389), Map(576,389), Map(618,389), Map(660,389)],
       [Map(94,430), Map(136,430), Map(178,430), Map(220,430), Map(262,430), Map(304,430), Map(346,430), Map(388,430), Map(430,430), Map(472,430), Map(514,430), Map(556,430), Map(598,430), Map(640,430), Map(682,430)],
       [Map(72,471), Map(114,471), Map(156,471), Map(198,471), Map(240,471), Map(282,471), Map(324,471), Map(366,471), Map(408,471), Map(450,471), Map(492,471), Map(534,471), Map(576,471), Map(618,471), Map(660,471)],
       [Map(94,512), Map(136,512), Map(178,512), Map(220,512), Map(262,512), Map(304,512), Map(346,512), Map(388,512), Map(430,512), Map(472,512), Map(514,512), Map(556,512), Map(598,512), Map(640,512), Map(682,512)]]

class Units:
    def __init__(self, name, quantity, is_player2 = False):
        self.name = name    # имя юнита
        self.quantity = quantity    # количество юнитов
        self.speed = 0    # скорость юнита
        self.stand = None    # Класс, который знает как правильно рисовать юнита относительно клетки где он стоит
        self.cell = None    # в какой клеточке стоит юнит
        self.cell2 = None
        self.is_two_cell = False    # юнит занимает две клетки?
        self.is_player2 = is_player2    # юнит справа? (вражеский?)

troops = Choosing_troops.start_selecting_troops(display, Units)
# нарезка спрайтов и закидывание их в объекты Units
Slicing_sprites.start(troops)
Characteristic_unit.start(troops)

# Начальная расстоновка войск (пока что в случаи если игрок поставит 0 войск, прокидывается ошибка. В дальнейшем можно вместо этого высвечивать игроку предупреждение в виде отдельного окна)
def deploy_troops(troops):
    troops_p1 = [unit for unit in troops[:7] if unit.name is not None]
    troops_p2 = [unit for unit in troops[7:] if unit.name is not None]

    if len(troops_p1) == 0:
        raise Exception("Войск не может быть 0!!!")
    elif len(troops_p1) == 1:
        for unit, m in zip(troops_p1, [map[5]]):
            if_two_cell(unit,m,False)    # функция определена ниже, она просто проверяет сколько клеток занимает персонаж, 1 или 2? И правильно назначает клетки
    elif len(troops_p1) == 2:
        for unit, m in zip(troops_p1, [map[0], map[10]]):
            if_two_cell(unit,m,False) 
    elif len(troops_p1) == 3:
        for unit, m in zip(troops_p1, [map[0], map[5], map[10]]):
            if_two_cell(unit,m,False) 
    elif len(troops_p1) == 4:
        for unit, m in zip(troops_p1, [map[0], map[4], map[6], map[10]]):
            if_two_cell(unit,m,False) 
    elif len(troops_p1) == 5:
        for unit, m in zip(troops_p1, [map[0],map[2],map[5],map[8],map[10]]):
            if_two_cell(unit,m,False) 
    elif len(troops_p1) == 6:
        for unit, m in zip(troops_p1, [map[0], map[2], map[4], map[6], map[8], map[10]]):
            if_two_cell(unit,m,False) 
    else:
        for unit, m in zip(troops_p1, [map[0], map[2], map[4], map[5], map[6], map[8], map[10]]):
            if_two_cell(unit,m,False) 

    if len(troops_p2) == 0:
        raise Exception("Войск не может быть 0!!!")
    elif len(troops_p2) == 1:
        for unit, m in zip(troops_p2, [map[5]]):
            if_two_cell(unit,m,True)
    elif len(troops_p2) == 2:
        for unit, m in zip(troops_p2, [map[0], map[10]]):
            if_two_cell(unit,m,True)
    elif len(troops_p2) == 3:
        for unit, m in zip(troops_p2, [map[0], map[5], map[10]]):
            if_two_cell(unit,m,True)
    elif len(troops_p2) == 4:
        for unit, m in zip(troops_p2, [map[0], map[4], map[6], map[10]]):
            if_two_cell(unit,m,True)
    elif len(troops_p2) == 5:
        for unit, m in zip(troops_p2, [map[0],map[2],map[5],map[8],map[10]]):
            if_two_cell(unit,m,True)
    elif len(troops_p2) == 6:
        for unit, m in zip(troops_p2, [map[0], map[2], map[4], map[6], map[8], map[10]]):
            if_two_cell(unit,m,True)
    else:
        for unit, m in zip(troops_p2, [map[0], map[2], map[4], map[5], map[6], map[8], map[10]]):
            if_two_cell(unit,m,True)

def if_two_cell(unit,m,enemy):
    if enemy:
        if unit.is_two_cell:
            unit.cell = m[13]
            unit.cell2 = m[14]
            m[13].unit = unit
            m[14].unit = unit
        else:
            unit.cell = m[14]
            m[14].unit = unit
    else:
        if unit.is_two_cell:
            unit.cell = m[1]
            unit.cell2 = m[0]
            m[1].unit = unit
            m[0].unit = unit
        else:
            unit.cell = m[0]
            m[0].unit = unit

deploy_troops(troops)

def sort(troops):    # сортирует войска по скорости, при этом чередуя вражеских и союзних юнитов с одинаковой скоростью
    troops = [unit for unit in troops if unit.name is not None]    # избавляемся от None
    friends = [unit for unit in troops if unit.is_player2 == False]    # разбиваем на две группы
    enemies = [unit for unit in troops if unit.is_player2 == True]
    friends = sorted(friends, key=lambda x: x.speed, reverse=True)    # сортируем каждую группу
    enemies = sorted(enemies, key=lambda x: x.speed, reverse=True)
    result = []
    i = j = 0
    while True:    # соединяем обе группы, чередуя вражеских и союзных юнитов с одинаковой скоростью
        if i >= len(friends):    # если закончились союзные юниты
            result.extend(enemies[j:])
            break
        if j >= len(enemies):    # если закончились вражеские юниты
            result.extend(friends[i:])
            break
        friend = friends[i]    # текущий вражеский и союзный юнит
        enemy = enemies[j]
        if friend.speed > enemy.speed:    # добавляем союзного юнита
            result.append(friend)
            i += 1
        elif enemy.speed > friend.speed:    # добавляем вражеского юнита
            result.append(enemy)
            j += 1
        else:                             # если скорости равны, добавляем обоих, тем самым чередуя их
            result.append(friend)
            result.append(enemy)
            i += 1
            j += 1
    return result

troops = sort(troops)
current_unit = troops[0]

while True:
    display.blit(background,(0,0))
    display.blit(panel, (0, 556))
    display.blit(grid,(70,100))

    mouse = pygame.mouse.get_pos()
    events = pygame.event.get()

    for line in map:
        for index, cell in enumerate(line):
            cell.render_current_unit()
            if cell.rect.collidepoint(mouse):
                cell.render_mouse_black()
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cell.unit == None:    # проверка того, что на клетку можно ходить
                            if current_unit.is_two_cell:    # вся логика передвижения юнитов
                                fifth = 0    # дабы юниты занимающие 2 клетки могли ходить в любую позицию, контролируем крайние ходы
                                if current_unit.is_player2:
                                    if index == 14:
                                        fifth = -1
                                    current_unit.cell.unit = None
                                    current_unit.cell2.unit = None
                                    current_unit.cell = line[index + fifth]
                                    current_unit.cell2 = line[index + 1 + fifth]
                                    line[index + fifth].unit = current_unit
                                    line[index + 1 + fifth].unit = current_unit
                                else:
                                    if index == 0:
                                        fifth = 1
                                    current_unit.cell.unit = None
                                    current_unit.cell2.unit = None
                                    current_unit.cell = line[index + fifth]
                                    current_unit.cell2 = line[index - 1 + fifth]
                                    line[index + fifth].unit = current_unit
                                    line[index - 1 + fifth].unit = current_unit
                            else:
                                current_unit.cell.unit = None
                                current_unit.cell = cell
                                cell.unit = current_unit
                            if id_current_unit == len(troops):    # передача хода следующему
                                id_current_unit = 0
                            current_unit = troops[id_current_unit]
                            id_current_unit += 1
            if cell.unit is not None:
                display.blit(cell.unit.stand.render,(cell.unit.cell.x + cell.unit.stand.x,cell.unit.cell.y + cell.unit.stand.y))    # рисует всех персонажей на поле исходя из того, где они стоят и поправки на отрисовку (юнитов занимающих 2 клетки рисуем дважды)



    pygame.display.update()

    for event in events:                                                 # обработка закрытия окна
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

