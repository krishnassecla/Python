import pygame


class Ship:
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""

        self.screen = screen

        # load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # load each new ship at the bottom center of the canvas
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Display the ship at its current location"""
        self.screen.blit(self.image, self.rect)
