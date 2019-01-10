import sys

import pygame

def check_events():
    '''react to key press and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    '''Update contents on the screen, and switch to new screen'''

    # redraw elements in the screen in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # refresh to display the latest drawn screen
    pygame.display.flip()


