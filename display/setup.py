import pygame, display, settings


def setup():
    pygame.init()

    display.upscaler.init()

    display.screen = pygame.display.set_mode([
        size * settings.SCREEN_SCALE for size in [
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT
        ]])

    return display
