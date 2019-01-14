import sys
import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # initiate game and create a screen object
    pygame.init()
    # create a Settings instance and set basic properties
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Space Invaders')

    # create a player ship
    ship = Ship(ai_settings, screen)
    # create a group to store bullets
    bullets = Group()

    # start main game loop
    while True:
        # supervise keyboard and mouse action
        gf.check_events(ai_settings, screen, ship, bullets)
        # update ship status
        ship.update()
        # update display contents in every frame
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
