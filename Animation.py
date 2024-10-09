import pygame as pg

pg.init()
screen = pg.display.set_mode((1000,100))
white = (255,255,255)
black = (0,0,0)
clock = pg.time.Clock()

class Kirby():

    def __init__ (self):
        self.hitbox = pg.Rect(485, 70, 30, 30)
        self.spd = 0
        self.frame = 0
        self.state = 0
        self.stdcount = 0

        self.std = []
        self.std.append(pg.image.load('X:\Angela\PY3\s1.png'))
        self.std.append(pg.image.load('X:\Angela\PY3\s2.png'))

        self.walkR = []
        self.walkR.append(pg.image.load('X:\Angela\PY3\w1.png'))
        self.walkR.append(pg.image.load('X:\Angela\PY3\w2.png'))
        self.walkR.append(pg.image.load('X:\Angela\PY3\w3.png'))
        self.walkR.append(pg.image.load('X:\Angela\PY3\w4.png'))
        self.walkR.append(pg.image.load('X:\Angela\PY3\w5.png'))
        self.walkR.append(pg.image.load('X:\Angela\PY3\w6.png'))

        self.walkL = []
        for x in self.walkR:
            self.walkL.append(pg.transform.flip(x, True, False))

    def draw(self):
        if self.state:
            if self.spd < 0:
                screen.blit(self.walkL[self.frame], (self.hitbox[0], self.hitbox[1]))
            else:
                screen.blit(self.walkR[self.frame], (self.hitbox[0], self.hitbox[1]))
        else:
            screen.blit(self.std[self.frame], (self.hitbox[0], self.hitbox[1]))

    def update(self):
        self.hitbox[0] += self.spd

        if self.spd != 0:
            self.state = 1
            self.frame += 1
            if self.frame > 5:
               self.frame =0
        else:
            self.state = 0
            if self.stdcount >= 20:
                self.stdcount = 0
                self.frame += 1
                if self.frame >= 2:
                    self.frame =0
            else:
                self.frame = 0
                self.stdcount+=1


kirb = Kirby()

while(1):
    pg.event.pump()

    #UPDATE
    kirb.update()

    #INPUT
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] == 1:
        kirb.spd = -5
    elif keys[pg.K_RIGHT] == 1:
        kirb.spd = 5
    else:
        kirb.spd = 0

    #DRAW
    screen.fill(white)
    kirb.draw()
    pg.display.flip()

    #TICK
    clock.tick(13)