class Settings:
    """A class to store all the settings for the game"""

    def __init__(self):
        """Initialize the game settings"""

        # bullet settings
        self.bullet_speed_factor = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 0.4
