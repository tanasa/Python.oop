# Card Class

import pygwidgets

class Card():

    def __init__(self, window, rank, suit, value):
        # must add code here to save away parameters in instance variables
        # and create two Image objects, one for the current card, one for the backOfCard
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        self.card_revealed = False  # Indicates if the card is showing its face or back
        self.location = (0, 0)      # Default location; can be set later

        # Set up the directory of pygwidgets.Image
        self.face_card_dir = f'images/{self.rank} of {self.suit}.png'
        self.back_card_dir = 'images/BackOfCard.png'

        # Initialize the images using pygwidgets.Image
        self.face_image = pygwidgets.Image(self.window, self.location, self.face_card_dir)
        self.back_image = pygwidgets.Image(self.window, self.location, self.back_card_dir)

    def conceal(self):
        # print('Must conceal the card here')
        self.card_revealed = False

    def setLoc(self, locTuple):
        print('Called setLoc method, passed in', locTuple)
        self.location = locTuple
        self.face_image.setLoc(locTuple)
        self.back_image.setLoc(locTuple)

    def reveal(self):
        # print('Must reveal card here')
        self.card_revealed = True

    def getName(self):
        print('Get the name of the card here')
        return f"{self.rank}  of {self.suit}"

    def getValue(self):
        print('Get the value of the card here')
        return self.value

    def draw(self):
        print('Draw the card here')
        if self.card_revealed:
           self.face_image.draw()
        else:
           self.back_image.draw()

    # No need to change this
    def getCardNameAndValue(self):
        return ("CardName", 0)