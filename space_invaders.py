import sys
import pygame

from settings import Settings

def run_game():
    # initiate game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Space Invaders')

    # start main game loop
    while True:

        # supervise keyboard and mouse action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # refill the screen with bg_color
        screen.fill(ai_settings.bg_color)

        # refresh to display the latest drawn screen
        pygame.display.flip()

run_game()
