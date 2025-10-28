import pygame, sys

display = pygame.display.set_mode((800,600))
background = pygame.image.load("image/Backgrounds/CmBkGrMt.png").convert_alpha()
panel = pygame.image.load("image/Panel.png").convert_alpha()
grid = pygame.image.load("image/grid.png").convert_alpha()
mouse_black = pygame.image.load("image/mouse_black.png").convert_alpha()
grid.set_colorkey((255,255,255))
mouse_black.set_alpha(100)

Pikeman_goes = pygame.image.load("image/Units/Pikeman_goes0.png").convert_alpha()
Pikeman_goes_rect = Pikeman_goes.get_rect()
Pikeman_goes.set_colorkey((255,255,255))

mouse_cursor = pygame.image.load("image/MouseCursors.png").convert_alpha()
mouse_cursor_rect = pygame.Rect(8,9,17,18)
mouse_cursor = mouse_cursor.subsurface(mouse_cursor_rect)
mouse_cursor = pygame.transform.scale(mouse_cursor,(32,32))
mouse_cursor.set_colorkey((0,255,255))
cursor = pygame.cursors.Cursor((0,0),mouse_cursor.convert_alpha())
pygame.mouse.set_cursor(cursor)

# 90 325
Pikeman_goes_rect[0] = 90
Pikeman_goes_rect[1] = 325

while True:
    display.blit(panel,(0,0))
    display.blit(background,(0,0))
    display.blit(grid,(70,100))
    display.blit(Pikeman_goes,(Pikeman_goes_rect[0] - Pikeman_goes_rect[2] / 2, Pikeman_goes_rect[1] - Pikeman_goes_rect[3]))

    mouse_points = pygame.mouse.get_pos()

    for y in range(11):
        for x in range(15):
            if y in [1, 3, 5, 7, 9, 11] and 93 + (42 * x) - 22 <= mouse_points[0] <= 134 + (42 * x) - 22 and 101 + (41 * y) <= mouse_points[1] <= 141 + (41 * y):
                display.blit(mouse_black, (72 + (42 * x), 102 + (41 * y)))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Pikeman_goes_rect[0] = 72 + (42 * x) + 20
                        Pikeman_goes_rect[1] = 102 + (41 * y) + 41
            elif y in [0,2,4,6,8,10] and 93 + (42 * x) <= mouse_points[0] <= 134 + (42 * x) and 101 + (41 * y) <= mouse_points[1] <= 141 + (41 * y):
                display.blit(mouse_black, (94 + (42 * x), 102 + (41 * y)))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Pikeman_goes_rect[0] = 72 + (42 * x) + 41
                        Pikeman_goes_rect[1] = 102 + (41 * y) + 41





    pygame.display.update()

    for event in pygame.event.get():                                                 # обработка закрытия окна
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()