import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # initiate game and create a screen object
    pygame.init()
    # create a Settings instance
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Space Invaders')

    # create a player ship
    ship = Ship(screen)

    # start main game loop
    while True:

        # supervise keyboard and mouse action
        gf.check_events()

        # redraw elements in the screen in every loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # refresh to display the latest drawn screen
        pygame.display.flip()

run_game()
