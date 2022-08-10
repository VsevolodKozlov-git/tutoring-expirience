import pygame
from pygame.sprite import Sprite
import math


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship, angle):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.angle = angle
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        dy = self.speed_factor * math.sin(math.radians(90 + self.angle))
        dx = self.speed_factor * math.cos(math.radians(90 + self.angle))
        self.y -= dy
        self.x += dx
        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
