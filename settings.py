class Settings():
    '''the class to store all the settings of Space Invaders'''

    def __init__(self):
        '''initiate STATIC game settings'''
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
        self.fleet_drop_speed = 100

        # game difficulty speed-up scale
        self.speedup_scale = 1.1

        # call dynamic settings method
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initialize DYNAMIC game settings'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1: move towards right
        # fleet_direction = -1: move towards left
        self.fleet_direction = 1

        # SCORE record
        self.alien_points = 50

    def increase_speed(self):
        '''speed increase settings'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
