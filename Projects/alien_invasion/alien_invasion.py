import sys
import pygame
from settings import Settings
from ship import Ship
import game_funtions as gf

# page : 282
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

    # main loop for the game
    while True:

        # watching for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
