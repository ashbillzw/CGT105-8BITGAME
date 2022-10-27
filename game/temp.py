from multiprocessing.util import ForkAwareThreadLock
import random, pygame, display

background1 = pygame.image.load("assets\\images\\background1.jpg")
background2 = pygame.image.load("assets\\images\\background2.jpg")
coinpng = pygame.image.load("assets\\images\\coin.png")
bombpng = pygame.image.load("assets\\images\\bomb.png")
gameoverpng = pygame.image.load("assets\\images\\gameover.png")

count = 0

playerX = 116
playerY = 104

pygame.font.init()
font = pygame.font.SysFont(None, 24)


class Item():
    def __init__(self, itemtype, x, y):
        self.itemtype = itemtype
        self.alive = True
        self.x = x
        self.y = y

    def update(self):
        global coincount, isGameOver, rollspeed

        self.x -= rollspeed
        if self.x < -24:
            self.alive = False
        
        if abs(self.x-playerX) < 20 and abs(self.y-(playerY+4)) < 20:
            self.alive = False
            if self.itemtype == "coin":
                if not isGameOver:
                    coincount += 1
            else:
                isGameOver = True

        display.screen.blit(coinpng if self.itemtype=="coin" else bombpng, (self.x, self.y))

items = []

isGameOver = False

coincount = 0

rollspeed = 2

flagSpawn = False

def update():
    global count, playerX, playerY, items, isGameOver, coincount, rollspeed, flagSpawn

    rollspeed = min(2 + coincount // 25, 8)

    count += rollspeed
    ind = count % 256

    display.screen.blit(background1, (-1 * ind, 0))
    display.screen.blit(background1, (-1 * ind + 256, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and playerY > 0:
        playerY -= 4
    if keys[pygame.K_a] and playerX > 0:
        playerX -= 2
    if keys[pygame.K_s] and playerY < 208:
        playerY += 4
    if keys[pygame.K_d] and playerX < 232:
        playerX += 2
    if keys[pygame.K_8]:
        coincount += 1
    if keys[pygame.K_r]:
        count = 0
        playerX = 116
        playerY = 104
        items = []
        isGameOver = False
        coincount = 0
        rollspeed = 2
        flagSpawn = False

    if count%256>(count+8)%256 and flagSpawn == False:
        flagSpawn = True
        f = random.random()
        if f < 0.9:
            big = random.randint(16, 200)
            for i in range(random.randint(3, 6)):
                items.append(Item(random.choice(["coin", "coin", "bomb"]), 288+i*48, big+random.randint(-16, 16)))
        if f < 0.3+min(coincount/400, 0.6):
            big = random.randint(48, 168)
            for i in range(random.randint(3, 6+coincount//20)):
                items.append(Item("bomb", 312+i*(48+coincount//3)+random.randint(-8, 8), big+random.randint(-48, 48)))
    if count%256<(count+8)%256: flagSpawn = False


    for i in items:
        i.update()
        if i.alive ==False:
            items.remove(i)


    pygame.draw.rect(display.screen, (180, 0, 200), (playerX, playerY, 24, 32))


    if isGameOver:
        display.screen.blit(gameoverpng, (0, 0))

    cc = font.render("Score: "+str(coincount), False, (255, 0, 0))
    display.screen.blit(cc, (144, 16))

    if rollspeed > 2:
        cc2 = font.render("Speed"+"+"*min(4, rollspeed-2), False, (255, 0, 0))
        display.screen.blit(cc2, (16, 16))
