import pygame
import random

class Ball:
    
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.ballImage = pygame.image.load("images/ball.png")

        ballRect = self.ballImage.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Random speeds between -3 and 3, excluding zero
        self.xSpeed = random.choice([-3, -2, -1, 1, 2, 3])
        self.ySpeed = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        # Check for wall collisions
        
        if (self.x < 0) or (self.x > self.maxWidth):
            self.xSpeed = -self.xSpeed
        if (self.y < 0) or (self.y > self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update ball position
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        self.window.blit(self.ballImage, (self.x, self.y))

    def reverse_direction(self):
        # Reverse both x and y speeds
        self.xSpeed = -self.xSpeed
        self.ySpeed = -self.ySpeed

    def is_clicked(self, mouse_pos):
        # Check if mouse click is within the ball's rectangle
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height
