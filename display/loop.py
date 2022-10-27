import pygame, display, game

def loop():
    while True:

        fpsClock = pygame.time.Clock()

        # Temporary Event-Handler
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
                raise RuntimeError

        # Fill Background
        display.screen.fill((255, 255, 255))
        display.screen.blit(pygame.image.load(".\\assets\\images\\background1.jpg"), (0, 0))

        game.temp.update()

        display.upscaler.update()

        pygame.display.update()

        fpsClock.tick(60)
