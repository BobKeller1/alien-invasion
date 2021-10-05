import sys
import pygame
from ship import Ship #
from bullet import Bullet


def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:  # 2
        # move the ship to the right
        ship.moving_right = True  # instead of changing the ship's position directly, we set it to True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):

    if len(bullets) <= ai_settings.bullets_allowed:

        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:  # when Right key is released, set the flag to False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen,ship, bullets):  # give ship parameter
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 1
            check_keydown_events(event, ai_settings, ship, screen, bullets)
        elif event.type == pygame.KEYUP:  # react to KEYUP events.
            check_keyup_events(event, ship)
            # ship.rect.centerx += 1  # 3
            # respond when key is pressed
            # if the pressed key is the right one, move the ship to the right by increasing the value of ship.rect.centerx by 1
            # isolate the event management loop so we can update the screen etc. seperately
def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)  # use the attribute of ai_settings
    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)