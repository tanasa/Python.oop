# Square class

import pygame
import random

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# To draw a rectangle instead of a square, we adjust the __init__ method to handle two dimensions
# (width and height) independently.
# We do not use the method : widthAndHeight !

class Rectangle():

    def __init__(self, window, maxWidth, maxHeight):

        self.window = window
        # self.widthAndHeight = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE))

        self.width = random.randrange(1, 100)   # Rectangle width
        self.height = random.randrange(1, 100)  # Rectangle height

        self.x = random.randrange(1, maxWidth - self.width)
        self.y = random.randrange(25, maxHeight - self.height)

        # self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight,
        #                                         self.widthAndHeight)

        self.rect = pygame.Rect(self.x, self.y, self.height, self.width)

        self.shapeType = 'Rectangle'
        
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getType(self):
        return self.shapeType
    
    def getArea(self):
        theArea = self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
