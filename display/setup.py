import pygame, display, settings


def setup():
    pygame.init()

    display.upscaler.init()

    display.screen = pygame.display.set_mode((
        settings.SCREEN_WIDTH,
        settings.SCREEN_HEIGHT
    ))

    return display
