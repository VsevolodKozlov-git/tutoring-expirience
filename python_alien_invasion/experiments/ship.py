from experiments.settings import Settings
import pygame
from math import ceil

class Ship:
    """
    Класс корабля, который умеет двигаться во все стороны
     |
    - -
     |

    """
    def __init__(self, screen: pygame.Surface, settings: Settings):
        self.screen = screen


        # Загружаем спрайт
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Размещаем его по центру
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Задаем направление корабля вектором
        self.direction_x = 0
        self.direction_y = 0
        self.ship_speed_factor = settings.ship_speed_factor

    def update(self, dt):
        """
            Обновляет положение корабля в зависимости от направления
            Также следит за тем, чтобы корабль не выпал за экран
        """
        dx = ceil(self.direction_x * dt * self.ship_speed_factor)
        dy = ceil(self.direction_y * dt * self.ship_speed_factor)
        # update positions of ship
        rect_after_move = self.rect.copy()
        rect_after_move = rect_after_move.move(dx, dy)
        # check ship position and update, if all right
        if  rect_after_move.left >= 0 and \
                rect_after_move.right <= self.screen_rect.right and \
                rect_after_move.bottom <= self.screen_rect.bottom and \
                rect_after_move.top >= 0:
            self.rect = rect_after_move



    def blit_me(self):
        """
        Изменяет позицию корабля и проверяет, чтобы он не вышел за края экрана
        """
        self.screen.blit(self.image, self.rect)


