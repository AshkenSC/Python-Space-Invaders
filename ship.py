import pygame

class Ship():
    def __init__(self, screen):
        '''initiate ship and set initial location'''
        self.screen = screen

        # load ship image and get its rectangle shape
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put new ships at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''draw ship in the designated location'''
        self.screen.blit(self.image, self.rect)
