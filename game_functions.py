import sys

import pygame

def check_events(ship):
    '''react to key press and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # move left
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    '''Update contents on the screen, and switch to new screen'''

    # redraw elements in the screen in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # refresh to display the latest drawn screen
    pygame.display.flip()


