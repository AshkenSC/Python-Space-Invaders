import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, si_settings, screen, ship, bullets):
    '''react to key DOWN events'''
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_SPACE:
        # create a bullt and add it to 'bullets'
        fire_bullet(si_settings, screen, ship, bullets)
    if event.key == pygame.K_RIGHT:
        # move right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # move left
        ship.moving_left = True

def check_keyup_events(event, ship):
    '''react to key UP events'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(si_settings, screen, ship, bullets):
    '''react to key press and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, si_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(si_settings, screen, ship, aliens, bullets):
    '''Update contents on the screen, and switch to new screen'''

    # redraw elements in the screen in every loop
    screen.fill(si_settings.bg_color)
    # redraw all the bullets after player and enemies
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # refresh to display the latest drawn screen
    pygame.display.flip()

def update_bullets(bullets):
    '''update bullets' location and delete vanished bullets'''
    # update bullets' location
    bullets.update()

    # delete vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    print(len(bullets)) # inspect bullets' number

def fire_bullet(si_settings, screen, ship, bullets):
    if len(bullets) < si_settings.bullets_allowed:
        new_bullet = Bullet(si_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(si_settings, screen, aliens):
    '''create a group of aliens'''
    # create an alien and calculate how many aliens
    # can one line contain
    # alien distance == alien width

    alien = Alien(si_settings, screen)
    alien_width = alien.rect.width
    available_space_x = si_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # create the first line of aliens
    for alien_number in range(number_aliens_x):
        # create an alien and add it to current line
        alien = Alien(si_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

def get_number_aliens_x(si_settings, alien_width):

     available_space_x = si_settings.screen_width - 2 * alien_width
     