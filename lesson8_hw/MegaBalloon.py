

import pygame
import pygwidgets
from Balloon import Balloon
from playsound import playsound
import random

class MegaBalloon(Balloon):

    balloonImage = pygame.image.load('images/megaBalloon.png')
    squeakSoundPath = 'sounds/balloonSqueak.wav'
    popSoundPath = 'sounds/balloonPop.wav'

    def __init__(self, window, maxWidth, maxHeight, ID):
        self.clickCount = 0
        oImage = pygwidgets.Image(window, (0, 0), MegaBalloon.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Mega', 50, 1.0)  # Adjust as needed

    def clickedInside(self, mousePoint):

        """
        Clicks :
        - First two clicks play the squeak sound.
        - Third click pops the balloon and awards points.
        """

        # Create a rectangle around the balloon to detect clicks
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)

        if myRect.collidepoint(mousePoint):
            self.clickCount += 1
            if self.clickCount < 3:
                playsound(MegaBalloon.squeakSoundPath)
                return False, 0            # balloon not popped, no points
            else:
                playsound(MegaBalloon.popSoundPath)
                return True, self.nPoints  # balloon popped, award points
        else:
            return False, 0                # no click detected

