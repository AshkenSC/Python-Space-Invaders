import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''class managing bullets shot by player ship'''

    def __init__(self, ai_settings, screen, ship):
        '''create a bullet object at the player ship location'''
        super(Bullet, self).__init__()
        self.screen = screen

        # at first, create a rect at (0,0)
        # then set it to correct location (ship top)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet location in FLOAT type
        # to adjust bullet location more delicately
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''move bullet upwards'''
        # update FLOAT value representing bullet location
        self.y -= self.speed_factor
        # update location of the rectangle that represents bullet
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw bullets on the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)