import pygame, display

def loop():
    while True:

        # Temporary Event-Handler
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
                raise RuntimeError

        display.screen.fill((255, 255, 255))
        pygame.display.update()
