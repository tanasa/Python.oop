import pygame
import random

class Drop():
    
    def __init__(self, window, windowWidth, windowHeight):

        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.dropImage = pygame.image.load("images/drop.png")
        dropRect = self.dropImage.get_rect()
        self.width = dropRect[2]
        self.height = dropRect[3]

        # Set a random X position and start Y position above the window
        self.x = random.randint(0, self.windowWidth - self.width)
        self.y = random.randint(-self.windowHeight, 0)      # The coordinates start above the window

        # Random speed for falling straight down
        self.speed = random.randint(3, 6)

    def update(self):
        # Move the drop downwards
        self.y += self.speed

        # If the drop goes off the screen, recycle it to the top
        if self.y > self.windowHeight:
            self.y = random.randint(-self.windowHeight, 0)             # Reset above the window
            self.x = random.randint(0, self.windowWidth - self.width)  # Optional: randomize x position

    def draw(self):
        self.window.blit(self.dropImage, (self.x, self.y))