import pygame

class Ship():
    def __init__(self, si_settings, screen):
        '''initiate ship and set initial location'''
        self.screen = screen
        self.si_settings = si_settings

        # load ship image and get its rectangle shape
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put new ships at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # convert ship's 'center' attribute to FLOAT
        # because built-in 'centerx' is INT, need conversion
        # then pass the 'center' value back to the built-in 'centerx'
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''adjust ship's location according to movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.si_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.si_settings.ship_speed_factor

        # update player ship's position
        # pass the 'center' value back to the built-in 'centerx'
        self.rect.centerx = self.center

    def blitme(self):
        '''draw ship in the designated location'''
        self.screen.blit(self.image, self.rect)
