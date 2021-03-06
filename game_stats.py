class GameStats():
    '''a class tracking game stats info'''

    def __init__(self, si_settings):
        '''initialize stats info'''
        self.si_settings = si_settings
        self.reset_stats()

        # set game to INACTIVE when launched
        self.game_active = False

        # do NOT reset highscore in ANY case!
        self.high_score = 0

    def reset_stats(self):
        '''
        initialize possible changing stats info
        while game is running
        '''
        self.ships_left = self.si_settings.ship_limit
        self.score = 0
        self.level = 1