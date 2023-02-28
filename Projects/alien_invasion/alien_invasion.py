import sys
import pygame
from settings import Settings
from ship import Ship
import game_funtions as gf
from pygame.sprite import Group

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

    # make a ship
    ship = Ship(ai_settings, screen)

    # make a group to store bullets
    bullets = Group()
    # main loop for the game
    while True:

        # watching for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()

        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
