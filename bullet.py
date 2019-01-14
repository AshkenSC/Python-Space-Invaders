import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''class managing bullets shot by player ship'''

    def __init__(self, ai_settings, screen, ship):
        '''create a bullet object at the player ship location'''
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rect at (0,0), then set correct location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullets' location in FLOAT type
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor