# Star object

import pygame
import pygwidgets
import random


import random
import pygame

class Square():
    def __init__(self, window, loc, maxWidth, maxHeight):

        self.window = window
        self.x, self.y = loc

        # Random position within the allowed bounds
        # self.x = random.randrange(1, maxWidth - 100)
        # self.y = random.randrange(1, maxHeight - 100)

        # Initial size
        self.width = random.randint(10, 100)
        self.height = self.width  # Ensure it's a square

        # Color
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        # Animation parameters
        self.targetWidth = self.width
        self.targetHeight = self.height
        self.growthRateWidth = 0
        self.growthRateHeight = 0
        self.nFrames = 0

        # Render a square
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            self.targetWidth = random.randint(10, 100)
            self.targetHeight = self.targetWidth
            self.growthRateWidth = (self.targetWidth - self.width) / 10
            self.growthRateHeight = (self.targetHeight - self.height) / 10
            self.nFrames = 10

    def update(self):
        if self.nFrames > 0:
            self.width += self.growthRateWidth
            self.height += self.growthRateHeight
            self.nFrames -= 1

            self.rect.width = int(self.width)
            self.rect.height = int(self.height)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)