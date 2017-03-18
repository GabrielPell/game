import sys, pygame
import random
from player import Player
from missile import PlayMissile, MissileSmoke, MissleDebris

pygame.init()

# Define game essentials such as screen size, in game clock and images used in game.
displayX = 2000
displayY = 1000
background = 0, 0, 0
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
window = pygame.display.set_mode((displayX, displayY))
surface = pygame.Surface((window.get_width(), window.get_height())).convert_alpha()
windowClock = pygame.time.Clock()
sprgAll = pygame.sprite.Group()
sprgBulls = pygame.sprite.Group()
sprgMiss = pygame.sprite.Group()
sprgSmoke = pygame.sprite.Group()
sprgMissileDebris = pygame.sprite.Group()


# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y, fps, mspf):
#         super(Player, self).__init__()
#         self.playLocX = x
#         self.playLocY = y
#         self.rightBorder = displayX - 15
#         self.moveSpeed = 7
#         self.rateOfFire = 8
#         self.frames = fps
#         self.fireDelay = (self.frames / self.rateOfFire) * mspf
#         self.fireStartTime = 0
#         self.isLeft = False
#         self.isRight = False
#         self.isShoot = False
#         self.image = pygame.image.load("Images/Spaceship.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (self.playLocX, self.playLocY)
#
#     def moveLeft(self):
#         if self.isLeft == True and self.rect.center >= (10, self.playLocY):
#             self.playLocX -= self.moveSpeed
#             self.rect.center = (self.playLocX, self.playLocY)
#
#     def moveRight(self):
#         if self.isRight == True and self.rect.center <= (displayX - 10, self.playLocY):
#             self.playLocX += self.moveSpeed
#             self.rect.center = (self.playLocX, self.playLocY)
#
#     def shootbull(self, t):
#
#         if self.isShoot == True:
#             self.playBull = PlayBullet(self.playLocX, self.playLocY)
#             sprgAll.add(self.playBull)
#             sprgBulls.add(self.playBull)
#
#     def shootMiss(self):
#         self.playMiss = PlayMissile(self.playLocX, self.playLocY)
#         sprgAll.add(self.playMiss)
#         sprgMiss.add(self.playMiss)
#
#     def moveBull(self):
#         for self.playBull in sprgBulls:
#             self.playBull.move()
#
#     def moveMiss(self, chrono):
#         for self.playMiss in sprgMiss:
#             self.playMiss.move()
#             self.playMiss.createSmoke(chrono)
#
#     def bindings(self, queue):
#         for event in queue:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     self.isLeft = True
#                     self.isRight = False
#                 if event.key == pygame.K_RIGHT:
#                     self.isRight = True
#                     self.isLeft = False
#                 if event.key == pygame.K_z:
#                     self.isShoot = True
#                     self.fireStartTime = pygame.time.get_ticks()
#                     self.shootbull()
#                 if event.key == pygame.K_x:
#                     self.fireStartTime = pygame.time.get_ticks()
#                     self.shootMiss()
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT:
#                     self.isLeft = False
#                 if event.key == pygame.K_RIGHT:
#                     self.isRight = False
#                 if event.key == pygame.K_z:
#                     self.isShoot = False
#                     self.fireStartTime = 0


class PlayBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(PlayBullet, self).__init__()
        self.bullLocX = x
        self.bullLocY = y
        self.tilt = random.uniform(-0.5, 0.5)
        self.image = pygame.Surface([10, 10]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.center = (self.bullLocX, self.bullLocY)

    def move(self):
        self.bullLocX += self.tilt
        self.bullLocY -= 7
        self.rect.center = (self.bullLocX, self.bullLocY)
        if self.bullLocY <= 0:
            self.kill()


# class PlayMissile(pygame.sprite.Sprite):
#     def __init__(self, x, y, state):
#         super(PlayMissile, self).__init__()
#         self.missLocX = x
#         self.missLocY = y
#         self.smokeTime = 0
#         self.smokeDelay = 1
#         self.image = pygame.image.load("Images/Missile.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (self.missLocX, self.missLocY)
#         self.state = state
#
#     def move(self):
#         self.missLocY -= 5
#         self.rect.center = (self.missLocX, self.missLocY)
#         if self.missLocY <= -100:
#             self.kill()
#
#
#     def createSmoke(self, timer):
#         self.smokeTime += timer
#         if self.smokeTime >= self.smokeDelay:
#             self.missSmoke = MissileSmoke(self.missLocX, self.missLocY)
#             sprgAll.add(self.missSmoke)
#
#     def explode(self):
#         if self.missLocY <= 200:
#             self.kill()
#             for i in range(300):
#                 debris = MissleDebris(self.missLocX, self.missLocY)
#                 sprgAll.add(debris)
#                 sprgMissileDebris.add(debris)
#
#
# class MissileSmoke(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(MissileSmoke, self).__init__()
#         self.spread = random.uniform(-1, 1)
#         self.smokeStart = y + 16
#         self.smokeLocX = x
#         self.smokeLocY = y + 16
#         self.image = pygame.Surface([5, 5]).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.image.fill(GRAY)
#         self.rect.center = (self.smokeLocX, self.smokeLocY)
#
#     @staticmethod
#     def moveall():
#         for smoke in sprgSmoke:
#             MissileSmoke.move(smoke)
#
#     def move(self):
#         if self.smokeLocY == displayY or self.smokeLocX <= -10 or self.smokeLocX == displayX:
#             self.kill()
#         self.smokeLocX += self.spread
#         self.smokeLocY += 1
#         self.rect.center = (self.smokeLocX, self.smokeLocY)
#
#
# class MissleDebris(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(MissleDebris, self).__init__()
#         self.expStart = 0
#         self.fadeStart = 1000
#         self.expEnd = 5000
#         self.moveStart = random.uniform(0, 250)
#         self.alpha = 255
#         self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
#         self.decide = random.randint(1, 4)
#         self.spreadX = random.uniform(0, 10)
#         self.spreadY = random.uniform(0, 10)
#         self.debrisLocX = x
#         self.debrisLocY = y
#         self.image = pygame.Surface([5, 5], flags=pygame.SRCALPHA).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.image.fill(self.randomcolor)
#         self.rect.center = (self.debrisLocX, self.debrisLocY)
#
#     @staticmethod
#     def moveall(timer):
#         t = timer
#         for debris in sprgMissileDebris:
#             MissleDebris.move(debris, t)
#
#     def move(self, t):
#         self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
#         self.image.fill(self.randomcolor)
#         self.expStart += t
#
#         if self.expStart >= self.fadeStart:
#                 self.alpha = self.alpha * 0.994
#
#         if self.expStart >= self.moveStart:
#             if self.expStart >= self.expEnd:
#                 self.kill()
#
#             if self.debrisLocY == displayY or self.debrisLocX <= -10 or self.debrisLocX == displayX:
#                 self.kill()
#
#             if self.decide == 1:
#                 self.debrisLocX += self.spreadX
#                 self.debrisLocY += self.spreadY
#
#             if self.decide == 2:
#                 self.debrisLocX -= self.spreadX
#                 self.debrisLocY += self.spreadY
#
#             if self.decide == 3:
#                 self.debrisLocX -= self.spreadX
#                 self.debrisLocY -= self.spreadY
#
#             if self.decide == 4:
#                 self.debrisLocX += self.spreadX
#                 self.debrisLocY -= self.spreadY
#
#         self.rect.center = (self.debrisLocX, self.debrisLocY)
#     def explode(self):
#         if self.missLocY <= 200:
#             self.kill()
#             for i in range(300):
#                 debris = MissleDebris(self.missLocX, self.missLocY)
#                 sprgAll.add(debris)
#                 sprgMissileDebris.add(debris)
#
#
# class MissileSmoke(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(MissileSmoke, self).__init__()
#         self.spread = random.uniform(-1, 1)
#         self.smokeStart = y + 16
#         self.smokeLocX = x
#         self.smokeLocY = y + 16
#         self.image = pygame.Surface([5, 5]).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.image.fill(GRAY)
#         self.rect.center = (self.smokeLocX, self.smokeLocY)
#
#     @staticmethod
#     def moveall():
#         for smoke in sprgSmoke:
#             MissileSmoke.move(smoke)
#
#     def move(self):
#         if self.smokeLocY == displayY or self.smokeLocX <= -10 or self.smokeLocX == displayX:
#             self.kill()
#         self.smokeLocX += self.spread
#         self.smokeLocY += 1
#         self.rect.center = (self.smokeLocX, self.smokeLocY)
#
#
# class MissleDebris(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(MissleDebris, self).__init__()
#         self.expStart = 0
#         self.fadeStart = 1000
#         self.expEnd = 5000
#         self.moveStart = random.uniform(0, 250)
#         self.alpha = 255
#         self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
#         self.decide = random.randint(1, 4)
#         self.spreadX = random.uniform(0, 10)
#         self.spreadY = random.uniform(0, 10)
#         self.debrisLocX = x
#         self.debrisLocY = y
#         self.image = pygame.Surface([5, 5], flags=pygame.SRCALPHA).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.image.fill(self.randomcolor)
#         self.rect.center = (self.debrisLocX, self.debrisLocY)
#
#     @staticmethod
#     def moveall(timer):
#         t = timer
#         for debris in sprgMissileDebris:
#             MissleDebris.move(debris, t)
#
#     def move(self, t):
#         self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
#         self.image.fill(self.randomcolor)
#         self.expStart += t
#
#         if self.expStart >= self.fadeStart:
#                 self.alpha = self.alpha * 0.994
#
#         if self.expStart >= self.moveStart:
#             if self.expStart >= self.expEnd:
#                 self.kill()
#
#             if self.debrisLocY == displayY or self.debrisLocX <= -10 or self.debrisLocX == displayX:
#                 self.kill()
#
#             if self.decide == 1:
#                 self.debrisLocX += self.spreadX
#                 self.debrisLocY += self.spreadY
#
#             if self.decide == 2:
#                 self.debrisLocX -= self.spreadX
#                 self.debrisLocY += self.spreadY
#
#             if self.decide == 3:
#                 self.debrisLocX -= self.spreadX
#                 self.debrisLocY -= self.spreadY
#
#             if self.decide == 4:
#                 self.debrisLocX += self.spreadX
#                 self.debrisLocY -= self.spreadY
#
#         self.rect.center = (self.debrisLocX, self.debrisLocY)
#     def explode(self):
#         if self.missLocY <= 200:
#             self.kill()
#             for i in range(300):
#                 debris = MissleDebris(self.missLocX, self.missLocY)
#                 sprgAll.add(debris)
#                 sprgMissileDebris.add(debris)
#
#
# class MissileSmoke(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(MissileSmoke, self).__init__()
#         self.spread = random.uniform(-1, 1)
#         self.smokeStart = y + 16
#         self.smokeLocX = x
#         self.smokeLocY = y + 16
#         self.image = pygame.Surface([5, 5]).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.image.fill(GRAY)
#         self.rect.center = (self.smokeLocX, self.smokeLocY)
#
#     @staticmethod
#     def moveall():
#         for smoke in sprgSmoke:
#             MissileSmoke.move(smoke)
#
#     def move(self):
#         if self.smokeLocY == displayY or self.smokeLocX <= -10 or self.smokeLocX == displayX:
#             self.kill()
#         self.smokeLocX += self.spread
#         self.smokeLocY += 1
#         self.rect.center = (self.smokeLocX, self.smokeLocY)
#
#
# class MissleDebris(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(MissleDebris, self).__init__()
#         self.expStart = 0
#         self.fadeStart = 1000
#         self.expEnd = 5000
#         self.moveStart = random.uniform(0, 250)
#         self.alpha = 255
#         self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
#         self.decide = random.randint(1, 4)
#         self.spreadX = random.uniform(0, 10)
#         self.spreadY = random.uniform(0, 10)
#         self.debrisLocX = x
#         self.debrisLocY = y
#         self.image = pygame.Surface([5, 5], flags=pygame.SRCALPHA).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.image.fill(self.randomcolor)
#         self.rect.center = (self.debrisLocX, self.debrisLocY)
#
#     @staticmethod
#     def moveall(timer):
#         t = timer
#         for debris in sprgMissileDebris:
#             MissleDebris.move(debris, t)
#
#     def move(self, t):
#         self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
#         self.image.fill(self.randomcolor)
#         self.expStart += t
#
#         if self.expStart >= self.fadeStart:
#                 self.alpha = self.alpha * 0.994
#
#         if self.expStart >= self.moveStart:
#             if self.expStart >= self.expEnd:
#                 self.kill()
#
#             if self.debrisLocY == displayY or self.debrisLocX <= -10 or self.debrisLocX == displayX:
#                 self.kill()
#
#             if self.decide == 1:
#                 self.debrisLocX += self.spreadX
#                 self.debrisLocY += self.spreadY
#
#             if self.decide == 2:
#                 self.debrisLocX -= self.spreadX
#                 self.debrisLocY += self.spreadY
#
#             if self.decide == 3:
#                 self.debrisLocX -= self.spreadX
#                 self.debrisLocY -= self.spreadY
#
#             if self.decide == 4:
#                 self.debrisLocX += self.spreadX
#                 self.debrisLocY -= self.spreadY
#
#         self.rect.center = (self.debrisLocX, self.debrisLocY)


class MainRun(object):
    def __init__(self):
        state = {
            'displayX': 2000,
            'displayY': 1000,
            'background': (0, 0, 0),
            'WHITE': (255, 255, 255),
            'GRAY': (127, 127, 127),
            'window': pygame.display.set_mode((displayX, displayY)),
            'surface': pygame.Surface((window.get_width(), window.get_height())).convert_alpha(),
            'windowClock': pygame.time.Clock(),
            'sprgAll': pygame.sprite.Group(),
            'sprgBulls': pygame.sprite.Group(),
            'sprgMiss': pygame.sprite.Group(),
            'sprgSmoke': pygame.sprite.Group(),
            'sprgMissileDebris': pygame.sprite.Group(),
            }
        self.Main(state)

    def Main(self, state):
        frameRate = 120
        msPerFrame = 1000/frameRate
        player1 = Player(1000, 900, frameRate, msPerFrame, state)
        sprgAll.add(player1)
        # When you work with classes you have to instantiate them,
        # which means you have to turn them into objects
        # you do this the way I did on the three lines below.
        # I instantiated them and assigned the new object to variables.
        # Further down you can see where I used those variables
        play_missile = PlayMissile(state)
        missile_smoke = MissileSmoke(state)
        missile_debris = MissleDebris(state)

        while True:
            eventqueue = pygame.event.get()
            for event in eventqueue:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            timer = windowClock.tick(frameRate)
            player1.bindings(eventqueue)
            player1.moveLeft()
            player1.moveRight()
            player1.moveBull()
            player1.moveMiss(timer)
            # I left your old method calls to show you the changes. 
            # You needed to add the @staticmethod wrapper previously
            # because you were not instantiating the class, so you didn't have 
            # an actual object to make the call on. The @staticmethod wrapper 
            # tells python to call the method directly on the class. 
            # You should be able to remove the @staticmethod wrappers doing it this way
            # This might help: https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
            # PlayMissile.checkExplode()
            play_missile.checkExplode()
            # MissileSmoke.moveall()
            missile_smoke.moveall()
            # MissleDebris.moveall(timer)
            missile_debris.moveall()
            player1.shootbull(timer)

            # if (pygame.time.get_ticks() - player1.fireStartTime) >= player1.fireDelay and player1.isShoot == True:
            #     player1.shootbull()
            #     player1.fireStartTime = pygame.time.get_ticks()

            sprgAll.clear(window, surface)
            sprgAll.draw(window)
            pygame.display.flip()

runGame = MainRun()
