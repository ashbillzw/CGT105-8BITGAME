import display, settings


def init():
    if settings.SCREEN_SCALE != 1:
        display.upscaler = Upscaler()

def update():
    return None

class Upscaler:
    def __init__(self):
        pass

    def update(self):
        pass
