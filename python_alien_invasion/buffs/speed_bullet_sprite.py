import pygame
class Alien(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.image = pygame.image.load('../chapter_13/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

        self.settings = ai_game.ai_settings
        self.screen  = ai_game.screen

    def update(self):
        speed = self.settings.fleet_speed_factor
        direction = self.settings.fleet_direction

        self.x += speed * direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.left < screen_rect.left or \
               self.rect.right > screen_rect.right

    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        return self.rect.bottom > screen_rect.bottom