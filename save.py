import pygame
import datetime
import sqlite3

con = sqlite3.connect("DataBase.db")
cursor = con.cursor()
titles = []
titles_name = []
rects_titles = []

def start(display, troops, index_current_unit):
    global titles
    global titles_name
    font = pygame.font.Font("font/timesnewromanpsmt.ttf", 20)
    font2 = pygame.font.Font("font/timesnewromanpsmt.ttf", 10)
    active = True
    save_name = ""
    current_rect = None

    cursor.execute("SELECT title FROM units")
    titles = cursor.fetchall()
    titles_name = []              # временно, для проверки дублей
    for title in titles:
        titles_name.append(title[0])

    for i in range(len(titles)):                                                    # собираем все имеющиеся rect
        rects_titles.append(pygame.Rect(210, 75 + i * 30, 380, 25))

    # область триггера кнопок
    save_button = pygame.Rect(210, 520, 185, 25)
    back_button = pygame.Rect(405, 520, 185, 25)

    while active:
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    save_name = save_name[:-1]
                elif event.unicode.isprintable() and len(save_name) < 30:
                    save_name += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if save_button.collidepoint(mouse):
                    if len(titles) != 10 and save_name not in titles_name:
                        add_sql(save_name, troops, index_current_unit)
                elif back_button.collidepoint(mouse):
                    active = False
        
        pygame.draw.rect(display, (80, 80, 80), (200, 50, 400, 500))          # фон основного окна 
        pygame.draw.rect(display, (200, 200, 200), (200, 50, 400, 500), 2)    # обводка основного окна

        max_save = font.render(f"{len(titles)}/10", True, (255, 255, 255))
        display.blit(max_save, (550, 50))

        if len(titles) != 0:
            for i in range(len(titles)):
                pygame.draw.rect(display, (200, 200, 200), (210, 75 + i * 30, 380, 25), 2)
                text_save = font.render(titles[i][0], True, (255, 255, 255))
                display.blit(text_save, (215, 75 + i * 30))
        
        for rect in rects_titles:                                  # наведения и нажатия на сохранения
            if rect.collidepoint(mouse):
                pygame.draw.rect(display, (255, 0, 0), rect, 2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_rect = rect
        if current_rect is not None:
            pygame.draw.rect(display, (255, 255, 200), current_rect, 2)


        pygame.draw.rect(display, (200, 200, 200), (210, 490, 380, 25), 2)    # поле input
        text_save = font.render(save_name, True, (255, 255, 255))
        display.blit(text_save, (215, 490))

        pygame.draw.rect(display, (200, 200, 200), (210, 520, 185, 25), 2)    # кнопка "сохранить"
        text_save = font.render("Сохранить", True, (255, 255, 255))
        display.blit(text_save, (250, 520))

        pygame.draw.rect(display, (200, 200, 200), (405, 520, 185, 25), 2)    # кнопка "назад"
        text_save = font.render("Назад", True, (255, 255, 255))
        display.blit(text_save, (470, 520))

        pygame.display.update()

def load(display):
    global titles
    font = pygame.font.Font("font/timesnewromanpsmt.ttf", 20)
    active = True
    current_rect = None

    cursor.execute("SELECT title FROM units")
    titles = cursor.fetchall()

    for i in range(len(titles)):                                                    # собираем все имеющиеся rect
        rects_titles.append(pygame.Rect(210, 75 + i * 30, 380, 25))

    # область триггера кнопок
    load_button = pygame.Rect(210, 520, 185, 25)
    back_button = pygame.Rect(405, 520, 185, 25)

    while active:
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if load_button.collidepoint(mouse):
                    if current_rect is not None:
                        id = rects_titles.index(current_rect) + 1
                        cursor.execute(f"SELECT * FROM units WHERE id={id}")
                        # print(cursor.fetchone())
                        return cursor.fetchone()
                elif back_button.collidepoint(mouse):
                    active = False
        
        pygame.draw.rect(display, (80, 80, 80), (200, 50, 400, 500))          # фон основного окна 
        pygame.draw.rect(display, (200, 200, 200), (200, 50, 400, 500), 2)    # обводка основного окна

        max_save = font.render(f"{len(titles)}/10", True, (255, 255, 255))
        display.blit(max_save, (550, 50))

        if len(titles) != 0:
            for i in range(len(titles)):
                pygame.draw.rect(display, (200, 200, 200), (210, 75 + i * 30, 380, 25), 2)
                text_save = font.render(titles[i][0], True, (255, 255, 255))
                display.blit(text_save, (215, 75 + i * 30))
        
        for rect in rects_titles:                                       # наведения и нажатия на сохранения
            if rect.collidepoint(mouse):
                pygame.draw.rect(display, (255, 0, 0), rect, 2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_rect = rect
        if current_rect is not None:
            pygame.draw.rect(display, (255, 255, 200), current_rect, 2)

        pygame.draw.rect(display, (200, 200, 200), (210, 520, 185, 25), 2)    # кнопка "загрузить"
        text_save = font.render("Загрузить", True, (255, 255, 255))
        display.blit(text_save, (250, 520))

        pygame.draw.rect(display, (200, 200, 200), (405, 520, 185, 25), 2)    # кнопка "назад"
        text_save = font.render("Назад", True, (255, 255, 255))
        display.blit(text_save, (470, 520))

        pygame.display.update()


def add_sql(save_name, troops, index_current_unit):
    global titles
    global rects_titles
    global titles_name
    names = ""
    quantities = ""
    is_player2 = ""
    cellx = ""
    celly = ""
    cell2x = ""
    cell2y = ""
    for troop in troops:
        names += str(troop.name) + ","
        quantities += str(troop.quantity) + ","
        is_player2 += str(troop.is_player2) + ","
        cellx += str(troop.cell.index_x) + ","
        celly += str(troop.cell.index_y) + ","
        if troop.cell2 is not None:
            cell2x += str(troop.cell2.index_x) + ","
            cell2y += str(troop.cell2.index_y) + ","
        else:
            cell2x += str(-1) + ","
            cell2y += str(-1) + ","
    names = names[:-1]
    quantities = quantities[:-1]
    is_player2 = is_player2[:-1]
    cellx = cellx[:-1]
    celly = celly[:-1]
    cell2x = cell2x[:-1]
    cell2y = cell2y[:-1]
    # print(troops[0].name, troops[0].quantity)
    cursor.execute(f"INSERT INTO units (title, name, quantity, is_player2, cellx, celly, cell2x, cell2y, index_current_unit) VALUES ('{save_name}','{names}', '{quantities}', '{is_player2}', '{cellx}','{celly}', '{cell2x}', '{cell2y}', {index_current_unit})")

    cursor.execute("SELECT title FROM units")
    titles = cursor.fetchall()

    rects_titles.append(pygame.Rect(210, 75 + (len(titles) - 1) * 30, 380, 25))

    titles_name = []              # временно, для проверки дублей
    for title in titles:
        titles_name.append(title[0])

    con.commit()  