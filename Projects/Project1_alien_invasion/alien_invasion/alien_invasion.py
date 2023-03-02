import sys
import pygame
from settings import Settings
from ship import Ship
import game_funtions as gf
from pygame.sprite import Group
from alien import Alien

# page : 298
def run_game():

    # create a screen object
    pygame.init()
    # alien invasion settings; create an instance of the class Settings
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of the aliens
    gf.create_fleet(ai_settings, screen, aliens)
    # main loop for the game
    # make an alien
    alien = Alien(ai_settings, screen)
    while True:

        # watching for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()

        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
