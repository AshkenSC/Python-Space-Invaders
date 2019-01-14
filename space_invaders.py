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
    si_settings = Settings()
    screen = pygame.display.set_mode(
        (si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption('Space Invaders')

    # create a player ship
    ship = Ship(si_settings, screen)
    # create a group to store bullets
    bullets = Group()

    # start main game loop
    while True:
        # supervise keyboard and mouse action
        gf.check_events(si_settings, screen, ship, bullets)
        # update objects' status
        ship.update()
        bullets.update()

        # delete vanished bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))     # inspect bullet number

        # update display contents in every frame
        gf.update_screen(si_settings, screen, ship, bullets)

run_game()
