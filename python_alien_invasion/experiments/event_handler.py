import pygame
import sys
from experiments.ship import  Ship


def check_all_events(ship: Ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            check_ship_events(event, ship)



def check_ship_events(event: pygame.event.Event, ship: Ship):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.direction_x = 1
        elif event.key == pygame.K_LEFT:
            ship.direction_x = -1
        elif event.key == pygame.K_UP:
            ship.direction_y = -1
        elif event.key == pygame.K_DOWN:
            ship.direction_y = 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or \
           event.key == pygame.K_RIGHT:
            ship.direction_x = 0
        if event.key == pygame.K_UP or \
           event.key == pygame.K_DOWN:
            ship.direction_y = 0
