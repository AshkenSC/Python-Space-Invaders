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
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 2.5
        self.bullet_width = 200
        self.bullet_height = 18
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 100
        # fleet_direction = 1: move towards right
        # fleet_direction = -1: move towards left
        self.fleet_direction = 1
