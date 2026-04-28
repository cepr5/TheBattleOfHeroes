import pygame
import sys
import save

pygame.init()

main_window = pygame.image.load("image/settings.png")

back_button = pygame.Rect(513, 469, 100, 47)
save_button = pygame.Rect(291, 469, 100, 47)
load_button = pygame.Rect(180, 469, 100, 47)

def start(display, troops, index_current_unit):
    settings = True
    while settings:
        display.blit(main_window, (155,50))
        # pygame.draw.rect(display, (255, 0, 0), (180, 469, 100, 47))
        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse):
                    settings = False
                if save_button.collidepoint(mouse):
                    save.start(display, troops, index_current_unit)
                if load_button.collidepoint(mouse):
                    load = save.load(display)
                    if load is not None:
                        return load





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
        
        pygame.display.update()