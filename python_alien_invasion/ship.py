import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        """
         Сначала переместим корабль, а потом проверим вышле ли он за границы
         Если вышел, то вернем его в прежнее положение
        """
        test_rect = self.rect.copy()
        new_center = self.center

        if self.moving_right:
            new_center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            new_center -= self.ai_settings.ship_speed_factor
        test_rect.centerx = new_center

        if test_rect.right < self.screen_rect.right and test_rect.left > 0:
            self.center = new_center

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
