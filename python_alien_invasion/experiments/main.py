import pygame
from pygame.sprite import Group
from experiments.settings import Settings
from experiments import event_handler
from experiments.ship import Ship
import sys


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption(settings.caption)
    clock = pygame.time.Clock()

    ship = Ship(screen, settings)
    while True:
        dt_sec = clock.tick(settings.fps) / 1000
        event_handler.check_all_events(ship)
        ship.update(dt_sec)
        screen.fill(settings.bg_color)
        ship.blit_me()
        pygame.display.flip()



if __name__ == '__main__':
    run_game()