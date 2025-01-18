# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball_extra_challenge import Ball
from Drop import Drop

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets
oInstructions = pygame.image.load('images/instructions.jpg')

# 5 - Initialize variables
ballList = []
dropList = []

# 6 - Main game loop
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                newBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                ballList.append(newBall)
            elif event.key == pygame.K_d:
                newDrop = Drop(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                dropList.append(newDrop)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for oBall in ballList:
                if oBall.is_clicked(mouse_pos):
                    oBall.reverse_direction()

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()
    for oDrop in dropList:
        oDrop.update()

    # 9 - Clear the screen
    window.fill(BLACK)
    
    # 10 - Draw elements
    window.blit(oInstructions, (85, 430))
    for oBall in ballList:
        oBall.draw()
    for oDrop in dropList:
        oDrop.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Control the frame rate
    clock.tick(FRAMES_PER_SECOND)
