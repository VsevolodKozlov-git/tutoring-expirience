class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed_factor = 1

        # Alien settings
        self.fleet_speed_factor = 0.5
        self.fleet_direction = 1
        self.fleet_drop_distance = 15

        # Bullet settings.
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        self.bullet_angle = 10

        # game settings.
        self.ship_limit = 3

        # buff settings
        self.speed_bullet_duration = 3
