import sys
import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard

def run_game():
    '''initiate game and create a screen object'''
    pygame.init()
    # create a Settings instance and set basic properties
    si_settings = Settings()
    screen = pygame.display.set_mode(
        (si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption('Space Invaders')

    # create PLAY button
    play_button = Button(si_settings, screen, "PLAY")

    # create an instance to store game stats and create a scoreboard
    stats = GameStats(si_settings)
    sb = Scoreboard(si_settings, screen, stats)

    '''create game object instances'''
    # create a player ship
    ship = Ship(si_settings, screen)
    # create a group to store bullets
    bullets = Group()
    # create an alien fleet
    aliens = Group()

    # create a group of aliens
    gf.create_fleet(si_settings, screen, ship, aliens)

    '''start main game loop'''
    while True:
        # supervise keyboard and mouse action
        gf.check_events(si_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
        # update objects' status
            ship.update()
            gf.update_bullets(si_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(si_settings, screen, stats, sb, ship, aliens, bullets)

        # update display contents in every frame
        gf.update_screen(si_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
