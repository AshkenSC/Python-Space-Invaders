import sys

import pygame

def check_keydown_events(event, ship):
    '''react to key DOWN events'''
    if event.key == pygame.K_RIGHT:
        # move right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # move left
        ship.moving_left = True

def check_keyup_events(event, ship):
    '''react to key UP events'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''react to key press and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    '''Update contents on the screen, and switch to new screen'''

    # redraw elements in the screen in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # refresh to display the latest drawn screen
    pygame.display.flip()


