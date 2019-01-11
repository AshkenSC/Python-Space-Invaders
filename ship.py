import pygame

class Ship():
    def __init__(self, screen):
        '''initiate ship and set initial location'''
        self.screen = screen

        # load ship image and get its rectangle shape
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put new ships at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # movement flag
        self.moving_right = False

    def update(self):
        '''adjust ship's location according to movement flag'''
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        '''draw ship in the designated location'''
        self.screen.blit(self.image, self.rect)
