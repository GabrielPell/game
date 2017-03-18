import pygame
from missile import PlayMissile
#from Game import PlayBullet, PlayMissile, MissileSmoke, MissleDebris

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, fps, mspf, state):
        super(Player, self).__init__()
        print state
        self.playLocX = x
        self.playLocY = y
        self.rightBorder = state['displayX'] - 15
        self.moveSpeed = 7
        self.rateOfFire = 8
        self.frames = fps
        self.fireDelay = (self.frames / self.rateOfFire) * mspf
        self.fireStartTime = 0
        self.isLeft = False
        self.isRight = False
        self.isShoot = False
        self.image = pygame.image.load("Images/Spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.playLocX, self.playLocY)
        self.state = state

    def moveLeft(self):
        if self.isLeft == True and self.rect.center >= (10, self.playLocY):
            self.playLocX -= self.moveSpeed
            self.rect.center = (self.playLocX, self.playLocY)

    def moveRight(self):
        if self.isRight == True and self.rect.center <= (self.state['displayX'] - 10, self.playLocY):
            self.playLocX += self.moveSpeed
            self.rect.center = (self.playLocX, self.playLocY)

    def shootbull(self, t):

        if self.isShoot == True:
            self.playBull = PlayBullet(self.playLocX, self.playLocY)
            self.state['sprgAll'].add(self.playBull)
            state['sprgBulls'].add(self.playBull)

    def shootMiss(self):
        self.playMiss = PlayMissile(self.playLocX, self.playLocY)
        self.state['sprgAll'].add(self.playMiss)
        self.state['sprgMiss'].add(self.playMiss)

    def moveBull(self):
        for self.playBull in self.state['sprgBulls']:
            self.playBull.move()

    def moveMiss(self, chrono):
        for self.playMiss in self.state['sprgMiss']:
            self.playMiss.move()
            self.playMiss.createSmoke(chrono)

    def bindings(self, queue):
        for event in queue:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.isLeft = True
                    self.isRight = False
                if event.key == pygame.K_RIGHT:
                    self.isRight = True
                    self.isLeft = False
                if event.key == pygame.K_z:
                    self.isShoot = True
                    self.fireStartTime = pygame.time.get_ticks()
                    self.shootbull()
                if event.key == pygame.K_x:
                    self.fireStartTime = pygame.time.get_ticks()
                    self.shootMiss()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.isLeft = False
                if event.key == pygame.K_RIGHT:
                    self.isRight = False
                if event.key == pygame.K_z:
                    self.isShoot = False
                    self.fireStartTime = 0
