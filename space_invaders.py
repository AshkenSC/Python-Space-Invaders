import sys
import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
    '''initiate game and create a screen object'''
    pygame.init()
    # create a Settings instance and set basic properties
    si_settings = Settings()
    screen = pygame.display.set_mode(
        (si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption('Space Invaders')

    '''create game object instances'''
    # create a player ship
    ship = Ship(si_settings, screen)
    # create a group to store bullets
    bullets = Group()
    # create an alien
    alien = Alien(si_settings, screen)

    '''start main game loop'''
    while True:
        # supervise keyboard and mouse action
        gf.check_events(si_settings, screen, ship, bullets)
        # update objects' status
        ship.update()
        gf.update_bullets(bullets)

        # update display contents in every frame
        gf.update_screen(si_settings, screen, ship, alien, bullets)

run_game()
