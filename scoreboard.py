import pygame.font

class Scoreboard():
    '''the class to display score'''

    def __init__(self, si_settings, screen, stats):
        '''initialize score-related attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.si_settings = si_settings
        self.stats = stats

        # set FONT of the score info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # get ready for initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        '''transform score DATA into a rendered IMAGE'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.si_settings.bg_color)

        # put score at top-right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''show score on the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        '''transform high score DATA into a rendered IMAGE'''
        high_score = int(round(self.stats.high_score, -1))
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.si_settings.bg_color)

        # put high score at top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
