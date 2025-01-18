#!/usr/bin/env python
# coding: utf-8

#  HigherOrLower


# In[1]:


import os
import sys
import random


# In[2]:


# Card constants
SUIT_TUPLE = ('Hearts', 'Clubs', 'Diamonds', 'Spades', )
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

# Define the Hierarchy for Tiebreakers
TIEBREAKER_HIERARCHY = {'Spades': 4, 'Diamonds': 3, 'Clubs': 2, 'Hearts': 1}




# In[3]:


# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pops one off the top of the deck and returns
    return thisCard
    
# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

#  Main code
print('Welcome to Higher Or Lower')
print('You have to choose if the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points, get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()


# In[4]:


# writing a function that creates the Deck List


# In[5]:


def DeckList(suit_tuple, rank_tuple):
    startingDeckList = []
    for suit in suit_tuple:
        for thisValue, rank in enumerate(rank_tuple):
            cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
            startingDeckList.append(cardDict)

    # Adding two Jokers
    joker_spades = {'rank': 'Joker', 'suit': 'Spades', 'value': 14}
    joker_hearts = {'rank': 'Joker', 'suit': 'Hearts', 'value': 14}
    startingDeckList.append(joker_spades)
    startingDeckList.append(joker_hearts)
    
    return startingDeckList


# In[6]:


NCARDS = 8
score = 50


while True:  
    print()
    startingDeckList = DeckList(SUIT_TUPLE,RANK_TUPLE)
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(NCARDS):   # play one game of this many cards

    
        answer = input('Will the next card be higher or lower than the ' + 
                               currentCardRank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()      # force lower case
    
        nextCardDict = getCard(gameDeckList)
        # print(nextCardDict)

        
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit, 'with a value of ' + str(nextCardValue) )

        # Determine if the guess is correct
        if (answer == 'h' and (nextCardValue > currentCardValue or 
                                (nextCardValue == currentCardValue and 
                                 TIEBREAKER_HIERARCHY[nextCardSuit] > TIEBREAKER_HIERARCHY[currentCardSuit]))) or \
           (answer == 'l' and (nextCardValue < currentCardValue or 
                                (nextCardValue == currentCardValue and 
                                 TIEBREAKER_HIERARCHY[nextCardSuit] < TIEBREAKER_HIERARCHY[currentCardSuit]))):
            print('You got it right!')
            score += 20
        else:
            print('Sorry, that was incorrect.')
            score -= 15

        # Print the score
        print('Your score is:', score)
        print()
        
        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ').strip().lower()
    if goAgain == 'q':
        break
print('OK bye')





