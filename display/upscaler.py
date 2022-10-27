import pygame, display, settings


def init():
    if settings.SCREEN_SCALE != 1:
        display.upscaler = Upscaler()

def update():
    return None

class Upscaler:
    def update(self):
        sw = settings.SCREEN_WIDTH
        sh = settings.SCREEN_HEIGHT
        ss = settings.SCREEN_SCALE

        display.screen.blit(
            pygame.transform.scale(
                display.screen.subsurface(0, 0, sw, sh),
                [size * ss for size in [sw, sh]]
            ), (0, 0)
        )
