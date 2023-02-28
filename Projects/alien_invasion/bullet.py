import pygame
from pygame.sprite import Sprite

# When you use sprites, you can group related elements in your game and act on all the grouped elements at once
class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        # you can reference to page 291 if you dont understand reading the code again.
        """Create bullet object at the ships position"""
        super(Bullet, self).__init__()
        # super().__init__()
        self.screen = screen

        # create bullet rect at 0,0 and then set the correct position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        # we are not using an image of the bullet so we need to create it from the scratch
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # update the decimal position of the bullet
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
