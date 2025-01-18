# Star object

import pygame
import pygwidgets
import random


class Frisbee():
    def __init__(self, window, loc):
        self.image = pygwidgets.Image(window, loc, 'images/Frisbee.png')
        self.startX = loc[0]
        self.startY = loc[1]
        self.x = self.startX
        self.y = self.startY
        self.rect = self.image.getRect()
        self.moving = False
        self.rotation = False
        self.angle = 0

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.speedX = random.randrange(-10, 10)
            self.speedY = random.randrange(-10, 10)
            self.nFrames = 30
            self.moving = True
            self.rotation = True
            self.angle=15

    def update(self):
        if not self.moving:
            return

        if self.moving :
           self.x = self.x + self.speedX
           self.y = self.y + self.speedY
           #print('New loc is:', (self.loc)
           self.image.setLoc((self.x, self.y))
           self.nFrames = self.nFrames - 1
           if  self.nFrames == 0:
               self.moving = False
               self.rect = self.image.getRect()

        if self.rotation:
            # Rotate the Frisbee
            self.image.rotate(self.angle)
            self.nFrames -= 1
            if self.nFrames == 0:
                self.rotation = False

    # This method is only needed in the Star class
    # def reset(self):
    #    self.x = self.startX
    #    self.y = self.startY
    #    self.image.setLoc((self.x, self.y))

    def draw(self):
        self.image.draw()