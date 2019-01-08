import sys
import pygame

def run_game():
    # initiate game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Space Invaders')

    # start main game loop
    while True:

        # supervise keyboard and mouse action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # let latest drawn screen visible
        pygame.display.flip()

run_game()
