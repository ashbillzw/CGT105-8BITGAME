import display


SCREEN_WIDTH = 256
SCREEN_HEIGHT = 240

import pygame

def setup():
    pygame.init()

    display.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    return display
