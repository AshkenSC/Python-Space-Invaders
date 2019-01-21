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

    def check_edges(self):
        '''restrict aliens' movement area'''
        '''if aliens are at the border of screen return True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''move aliens towards right OR left'''
        self.x += (self.si_settings.alien_speed_factor *
                    self.si_settings.fleet_direction)
        self.rect.x = self.x