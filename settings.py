class Settings():
    '''the class to store all the settings of Space Invaders'''

    def __init__(self):
        '''initiate game settings'''
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # player ship settings
        self.ship_speed_factor = 2.0

        # bullet settings
        self.bullet_speed_factor = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
