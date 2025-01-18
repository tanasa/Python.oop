# Catch the fruit

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from Fruit import *  # bring in the Fruit class code
from Basket import * # bring

# 2 - Define constants
BLACK = (0, 0, 0)
LIME = (0, 255,0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
oDisplay = pygwidgets.DisplayText(window, (WINDOW_WIDTH -120, 10), '', fontSize=30)

# 5 - Initialize variables
backgroundImage = pygwidgets.Image(window, (0, 0), 'images/background.png')
oBasket = Basket(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# oFruit = Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'apple')

# Create many types of fruits
fruits = [
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'apple', points=12),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'banana', points=10),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'cherry', points=13),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'grapes', points=11),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'strawberry', points=14),
    Fruit(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'pear', points=15)
]
oRestartButton = pygwidgets.TextButton(window, (5, 5), 'Restart')

score = 0


# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):  # it clicked on the Restart button
            print('User pressed the Restart button')
            score = 0
            for fruit in fruits:
                fruit.reset()                   # it resets each fruit's position

    # Add "continuous mode" code here to check for left or right arrow keys
    # If you get one, tell the basket to move itself appropriately

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        oBasket.move('left')
    elif keys[K_RIGHT]:
        oBasket.move('right')

    # 8 - Do any "per frame" actions
    # oFruit.update()  # tell each fruit to update itself

    basketRect = oBasket.getRect()

    # fruitRect = oFruit.getRect()

    # if basketRect.colliderect(fruitRect):
    #    print('Fruit has collided with the basket')

    for fruit in fruits:
        fruit.update()          # it updates each fruit’s position
        fruitRect = fruit.getRect()

        if basketRect.colliderect(fruitRect):
            points = fruit.getPoints()
            score += points
            fruit.reset()

        oDisplay.setValue('Score:' + str(score))

    # 9 - Clear the screen before drawing it again
    backgroundImage.draw()
    
    # 10 - Draw the screen elements
    # oFruit.draw()   # tell each ball to draw itself

    for fruit in fruits:
        fruit.draw()  # Draw each fruit

    oRestartButton.draw()
    oBasket.draw()
    oDisplay.draw()

    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
