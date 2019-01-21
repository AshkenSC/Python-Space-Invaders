import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''single alien class'''

    def __init__(self, si_settings, screen):
        '''initialize alien and its location'''
        super(Alien, self).__init__()
        self.screen = screen
        self.si_settings = si_settings

        # load alien image and set its RECT attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien is born at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store each alien's accurate position
        # transform position value to FLOAT
        self.x = float(self.rect.x)

    def blitme(self):
        '''draw alien at designated position'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''move aliens leftwards'''
        self.x += self.si_settings.alien_speed_factor
        self.rect.x = self.x