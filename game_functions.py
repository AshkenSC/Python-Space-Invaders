import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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

def check_events(si_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets):
    '''react to key press and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, si_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(si_settings, screen, stats, sb, play_button, ship, aliens,
                              bullets, mouse_x, mouse_y)

def check_play_button(si_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    '''start new game when player clicks on PLAY button'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game settings
        si_settings.initialize_dynamic_settings()

        # hide cursor
        pygame.mouse.set_visible(False)

        if play_button.rect.collidepoint(mouse_x, mouse_y):
            # reset game stats info
            stats.reset_stats()
            stats.game_active = True

            # reset scoreboard image
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()

            # clean aliens list and bullets list
            aliens.empty()
            bullets.empty()

            # create a new ALIEN fleet and set PLAYER at CENTER
            create_fleet(si_settings, screen, ship, aliens)
            ship.center_ship()


def update_screen(si_settings, screen, stats, sb, ship, aliens,
                  bullets, play_button):
    '''Update contents on the screen, and switch to new screen'''

    # redraw elements in the screen in every loop
    screen.fill(si_settings.bg_color)
    # redraw all the bullets after player and enemies
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # show SCORE
    sb.show_score()

    # if the game is INACTIVE, draw PLAY button
    if not stats.game_active:
        play_button.draw_button()

    # refresh to display the latest drawn screen
    pygame.display.flip()

def update_bullets(si_settings, screen, stats, sb, ship, aliens, bullets):
    '''update bullets' location and delete vanished bullets'''
    # update bullets' location
    bullets.update()

    # delete vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(si_settings, screen, stats, sb, ship,
                                  aliens, bullets)

def check_bullet_alien_collisions(si_settings, screen, stats, sb, ship,
                                  aliens, bullets):
    # check if any bullet hits alien
    # if so, delete the bullet and the alien
    '''
    CAUTION: if the booleans are set as 'False, True'
    then the bullet will PENETRATE all the aliens it collides
    '''
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += si_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # if the fleet is eliminated, raise level by 1
        # delete current bullets and create a new FLEET
        bullets.empty()
        si_settings.increase_speed()

        # raise level
        stats.level += 1
        sb.prep_level()

        create_fleet(si_settings, screen, ship, aliens)

def fire_bullet(si_settings, screen, ship, bullets):
    if len(bullets) < si_settings.bullets_allowed:
        new_bullet = Bullet(si_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(si_settings, screen, ship, aliens):
    '''create a group of aliens'''
    # create an alien and calculate how many aliens can one line contain
    # alien distance == alien width
    alien = Alien(si_settings, screen)
    number_aliens_x = get_number_aliens_x(si_settings, alien.rect.width)
    number_rows = get_number_rows(si_settings, ship.rect.height, alien.rect.height)

    # create the first line of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(si_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(si_settings, alien_width):
    '''calculate how many aliens can one line contain'''
    available_space_x = si_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(si_settings, screen, aliens, alien_number, row_number):
    '''create an alien and put it at current line'''
    alien = Alien(si_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(si_settings, ship_height, alien_height):
    '''calculate how many alien lines can the screen contain'''
    available_space_y = (si_settings.screen_height - (5 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(si_settings, aliens):
    '''reactions when aliens reach screen border'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(si_settings, aliens)
            break

def change_fleet_direction(si_settings, aliens):
    '''move alien fleet downwards and change their direction'''
    for alien in aliens.sprites():
        alien.rect.y += si_settings.fleet_drop_speed
    si_settings.fleet_direction *= -1

def ship_hit(si_settings, screen, stats, sb, ship, aliens, bullets):
    '''reactions of ship hit by aliens'''
    if stats.ships_left > 0:
        # ships_left -1
        stats.ships_left -= 1

        # update scoreboard
        sb.prep_ships()

        # clean alien list and bullet list
        aliens.empty()
        bullets.empty()

        # create a new alien fleet
        # put player ship at bottom center of the screen
        create_fleet(si_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(si_settings, screen, stats, sb, ship, aliens, bullets):
    '''check if any alien reaches the bottom of screen'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            # tackle like when PLAYER is hit
            ship_hit(si_settings, screen, stats, sb, ship, aliens, bullets)
            break

def update_aliens(si_settings, screen, stats, sb, ship, aliens, bullets):
    '''
    check if any alien is at screen border
    and update alien fleet's total location
    '''
    check_fleet_edges(si_settings, aliens)
    aliens.update()

    # check collision between PLAYER and ALIENS
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(si_settings, screen, stats, sb, ship, aliens, bullets)

    # check if any alien reaches the bottom of screen
    check_aliens_bottom(si_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    '''check if there is a NEW HIGH score'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()