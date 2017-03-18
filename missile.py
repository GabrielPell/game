import pygame
class PlayMissile(pygame.sprite.Sprite):
    def __init__(self, state):
        super(PlayMissile, self).__init__()
        self.missLocX = state['displayX']
        self.missLocY = state['displayY']
        self.smokeTime = 0
        self.smokeDelay = 1
        self.image = pygame.image.load("Images/Missile.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.missLocX, self.missLocY)
        self.state = state

    def move(self):
        self.missLocY -= 5
        self.rect.center = (self.missLocX, self.missLocY)
        if self.missLocY <= -100:
            self.kill()


    def createSmoke(self, timer):
        self.smokeTime += timer
        if self.smokeTime >= self.smokeDelay:
            self.missSmoke = MissileSmoke(self.missLocX, self.missLocY)
            self.state['sprgAll'].add(self.missSmoke)

    def checkExplode(self):
        for missile in self.state['sprgMiss']:
            missile.explode

    def explode(self):
        if self.missLocY <= 200:
            self.kill()
            for i in range(300):
                debris = MissleDebris(self.missLocX, self.missLocY)
                sprgAll.add(debris)
                sprgMissileDebris.add(debris)


class MissileSmoke(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MissileSmoke, self).__init__()
        self.spread = random.uniform(-1, 1)
        self.smokeStart = y + 16
        self.smokeLocX = x
        self.smokeLocY = y + 16
        self.image = pygame.Surface([5, 5]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(GRAY)
        self.rect.center = (self.smokeLocX, self.smokeLocY)

    # @staticmethod
    def moveall():
        for smoke in sprgSmoke:
            MissileSmoke.move(smoke)

    def move(self):
        if self.smokeLocY == displayY or self.smokeLocX <= -10 or self.smokeLocX == displayX:
            self.kill()
        self.smokeLocX += self.spread
        self.smokeLocY += 1
        self.rect.center = (self.smokeLocX, self.smokeLocY)


class MissleDebris(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MissleDebris, self).__init__()
        self.expStart = 0
        self.fadeStart = 1000
        self.expEnd = 5000
        self.moveStart = random.uniform(0, 250)
        self.alpha = 255
        self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
        self.decide = random.randint(1, 4)
        self.spreadX = random.uniform(0, 10)
        self.spreadY = random.uniform(0, 10)
        self.debrisLocX = x
        self.debrisLocY = y
        self.image = pygame.Surface([5, 5], flags=pygame.SRCALPHA).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(self.randomcolor)
        self.rect.center = (self.debrisLocX, self.debrisLocY)

    @staticmethod
    def moveall(timer):
        t = timer
        for debris in sprgMissileDebris:
            MissleDebris.move(debris, t)

    def move(self, t):
        self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
        self.image.fill(self.randomcolor)
        self.expStart += t

        if self.expStart >= self.fadeStart:
                self.alpha = self.alpha * 0.994

        if self.expStart >= self.moveStart:
            if self.expStart >= self.expEnd:
                self.kill()

            if self.debrisLocY == displayY or self.debrisLocX <= -10 or self.debrisLocX == displayX:
                self.kill()

            if self.decide == 1:
                self.debrisLocX += self.spreadX
                self.debrisLocY += self.spreadY

            if self.decide == 2:
                self.debrisLocX -= self.spreadX
                self.debrisLocY += self.spreadY

            if self.decide == 3:
                self.debrisLocX -= self.spreadX
                self.debrisLocY -= self.spreadY

            if self.decide == 4:
                self.debrisLocX += self.spreadX
                self.debrisLocY -= self.spreadY

        self.rect.center = (self.debrisLocX, self.debrisLocY)
    def explode(self):
        if self.missLocY <= 200:
            self.kill()
            for i in range(300):
                debris = MissleDebris(self.missLocX, self.missLocY)
                sprgAll.add(debris)
                sprgMissileDebris.add(debris)


class MissileSmoke(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MissileSmoke, self).__init__()
        self.spread = random.uniform(-1, 1)
        self.smokeStart = y + 16
        self.smokeLocX = x
        self.smokeLocY = y + 16
        self.image = pygame.Surface([5, 5]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(GRAY)
        self.rect.center = (self.smokeLocX, self.smokeLocY)

    @staticmethod
    def moveall():
        for smoke in sprgSmoke:
            MissileSmoke.move(smoke)

    def move(self):
        if self.smokeLocY == displayY or self.smokeLocX <= -10 or self.smokeLocX == displayX:
            self.kill()
        self.smokeLocX += self.spread
        self.smokeLocY += 1
        self.rect.center = (self.smokeLocX, self.smokeLocY)


class MissleDebris(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MissleDebris, self).__init__()
        self.expStart = 0
        self.fadeStart = 1000
        self.expEnd = 5000
        self.moveStart = random.uniform(0, 250)
        self.alpha = 255
        self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
        self.decide = random.randint(1, 4)
        self.spreadX = random.uniform(0, 10)
        self.spreadY = random.uniform(0, 10)
        self.debrisLocX = x
        self.debrisLocY = y
        self.image = pygame.Surface([5, 5], flags=pygame.SRCALPHA).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(self.randomcolor)
        self.rect.center = (self.debrisLocX, self.debrisLocY)

    @staticmethod
    def moveall(timer):
        t = timer
        for debris in sprgMissileDebris:
            MissleDebris.move(debris, t)

    def move(self, t):
        self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
        self.image.fill(self.randomcolor)
        self.expStart += t

        if self.expStart >= self.fadeStart:
                self.alpha = self.alpha * 0.994

        if self.expStart >= self.moveStart:
            if self.expStart >= self.expEnd:
                self.kill()

            if self.debrisLocY == displayY or self.debrisLocX <= -10 or self.debrisLocX == displayX:
                self.kill()

            if self.decide == 1:
                self.debrisLocX += self.spreadX
                self.debrisLocY += self.spreadY

            if self.decide == 2:
                self.debrisLocX -= self.spreadX
                self.debrisLocY += self.spreadY

            if self.decide == 3:
                self.debrisLocX -= self.spreadX
                self.debrisLocY -= self.spreadY

            if self.decide == 4:
                self.debrisLocX += self.spreadX
                self.debrisLocY -= self.spreadY

        self.rect.center = (self.debrisLocX, self.debrisLocY)
    def explode(self):
        if self.missLocY <= 200:
            self.kill()
            for i in range(300):
                debris = MissleDebris(self.missLocX, self.missLocY)
                sprgAll.add(debris)
                sprgMissileDebris.add(debris)


class MissileSmoke(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MissileSmoke, self).__init__()
        self.spread = random.uniform(-1, 1)
        self.smokeStart = y + 16
        self.smokeLocX = x
        self.smokeLocY = y + 16
        self.image = pygame.Surface([5, 5]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(GRAY)
        self.rect.center = (self.smokeLocX, self.smokeLocY)

    @staticmethod
    def moveall():
        for smoke in sprgSmoke:
            MissileSmoke.move(smoke)

    def move(self):
        if self.smokeLocY == displayY or self.smokeLocX <= -10 or self.smokeLocX == displayX:
            self.kill()
        self.smokeLocX += self.spread
        self.smokeLocY += 1
        self.rect.center = (self.smokeLocX, self.smokeLocY)


class MissleDebris(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(MissleDebris, self).__init__()
        self.expStart = 0
        self.fadeStart = 1000
        self.expEnd = 5000
        self.moveStart = random.uniform(0, 250)
        self.alpha = 255
        self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
        self.decide = random.randint(1, 4)
        self.spreadX = random.uniform(0, 10)
        self.spreadY = random.uniform(0, 10)
        self.debrisLocX = x
        self.debrisLocY = y
        self.image = pygame.Surface([5, 5], flags=pygame.SRCALPHA).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(self.randomcolor)
        self.rect.center = (self.debrisLocX, self.debrisLocY)

    @staticmethod
    def moveall(timer):
        t = timer
        for debris in sprgMissileDebris:
            MissleDebris.move(debris, t)

    def move(self, t):
        self.randomcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.alpha)
        self.image.fill(self.randomcolor)
        self.expStart += t

        if self.expStart >= self.fadeStart:
                self.alpha = self.alpha * 0.994

        if self.expStart >= self.moveStart:
            if self.expStart >= self.expEnd:
                self.kill()

            if self.debrisLocY == displayY or self.debrisLocX <= -10 or self.debrisLocX == displayX:
                self.kill()

            if self.decide == 1:
                self.debrisLocX += self.spreadX
                self.debrisLocY += self.spreadY

            if self.decide == 2:
                self.debrisLocX -= self.spreadX
                self.debrisLocY += self.spreadY

            if self.decide == 3:
                self.debrisLocX -= self.spreadX
                self.debrisLocY -= self.spreadY

            if self.decide == 4:
                self.debrisLocX += self.spreadX
                self.debrisLocY -= self.spreadY

        self.rect.center = (self.debrisLocX, self.debrisLocY)

