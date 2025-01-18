#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Square class - text based
# Allows you to change set initial data, then change the data, and show the square as text
# Because of fonts, squares will probably not show as exactly square

class Square():
    """Represents a square
    """

    def __init__(self, size, hChar, vChar, cornerChar):
        ''' Initializes a square
        Pass in the size, the character to used for the horizontal edge, vertical edge, and corners.
        '''
        self.size = size
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the square in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''
        
        if self.size < 2:
            raise ValueError("Size must be at least 2 to create a visible square.")
           
        print()
        
        # top edge
        print(self.cornerChar + (self.size - 2) * self.hChar + self.cornerChar)
        
        # middle portion
        for i in range(1, self.size-1):
            print(self.vChar + (self.size - 2) * " " + self.vChar)
        
        # bottom edge
        print(self.cornerChar + (self.size - 2) * self.hChar + self.cornerChar)

    def getSize(self):
        ''' Returns the size of an edge of the Square '''
        return self.size

    def setHorizontalChar(self, newHChar):
        ''' Set a new horizontal character '''
        self.hChar = newHChar
        
    def setVerticalChar(self, newVChar):
        ''' Set a new vertical character '''
        self.vChar = newVChar

    def setCornerChar(self, newCornerChar):
        ''' Set a new corner character '''
        self.cornerChar = newCornerChar

    # Must add 2 additional methods: setSize and getArea

    def setSize(self, newSize):
        if newSize < 2:
            raise ValueError("Size must be at least 2")
        self.size = newSize

    def getArea(self):
        return self.size *self.size  


# In[ ]:





# In[23]:


# Test code
# Create a square of size 5
oSquare1 = Square(5, '-', '|', '*')  # pass in size, horizonal, vertical, and edge characters
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())

# Create another square of size 10
oSquare2 = Square(10, '-', '|', '*')
oSquare2.show()
print('Size is:', oSquare2.getSize(), " area is:", oSquare2.getArea())

# Tell the first square to modify its data
oSquare1.setSize(7)
oSquare1.setHorizontalChar('^')
oSquare1.setVerticalChar('?')
oSquare1.setCornerChar('$')
oSquare1.show()
print('Size is:', oSquare1.getSize(), " area is:", oSquare1.getArea())
print()


# In[ ]:


# 2)  Add code to ask the user four questions that will define a square:

# a) What is the (integer) size of an edge of a square?
# b) What character to use for the horizontal edges?
# c) What character  to use for the vertical edges?
# d) What character  to use for the corners?


# In[25]:


def input_square_parameters():
    '''Prompts the user for parameters to create a Square.'''
    
    size = int(input("Please enter the size of the square: "))
    hChar = input("Please enter the character for the horizontal edges: ")
    vChar = input("Please enter a character for the vertical edges: ")
    cornerChar = input("Please enter a character for the corners: ")
    return size, hChar, vChar, cornerChar


def main():

    size, hChar, vChar, cornerChar = input_square_parameters()
    input_square = Square(size, hChar, vChar, cornerChar)
    input_square.show()


# Run the program
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:


# To solve the second part of the exercise :
# Consider what you you have to do to create a similar Rectangle class - would any methods need to be eliminated, 
# or added, and changes in parameters to methods?
# Modify the code to do what you need to do to make Rectangle objects.


# In[51]:


class Rectangle():
    
    """Represents a rectangle"""

    def __init__(self, width, length, hChar, vChar, cornerChar):
        ''' Initializes a rectangle
        Pass in the width and the length (height), and the character to used for 
        the horizontal edge, vertical edge, and corners.
        '''
        self.width = width
        self.length = length
        self.hChar = hChar
        self.vChar = vChar
        self.cornerChar = cornerChar

    def show(self):
        ''' Print the rectangle in text using the horizontal edge, vertical edge, and corner characters
        Use a space (' ') for all characters not on an edge
        '''
           
        print()
        
        # top edge
        print(self.cornerChar + (self.width - 2) * self.hChar + self.cornerChar)
        
        # middle portion
        for i in range(1, self.length-1):
            print(self.vChar + (self.width - 2) * " " + self.vChar)
        
        # bottom edge
        print(self.cornerChar + (self.width - 2) * self.hChar + self.cornerChar)

    def getDimensions(self):
        ''' Returns the width and the length of the rectangle'''
        return self.width, self.length

    def setHorizontalChar(self, newHChar):
        ''' Set a new horizontal character '''
        self.hChar = newHChar
        
    def setVerticalChar(self, newVChar):
        ''' Set a new vertical character '''
        self.vChar = newVChar

    def setCornerChar(self, newCornerChar):
        ''' Set a new corner character '''
        self.cornerChar = newCornerChar


    def setWidth(self, newWidth):
        if newWidth < 2:
            raise ValueError("Width must be at least 2")
        self.width = newWidth

    def setLength(self, newLength):
        if newLength < 2:
            raise ValueError("Length must be at least 2")
        self.length = newLength
        
    def getArea(self):
        return self.width *self.length 


# In[52]:


# Test code
# Create a rectangle of width 5 and height 3
oRectangle1 = Rectangle(5, 3, '-', '|', '*')  # pass in sizes, horizonal, vertical, and edge characters
oRectangle1.show()
print('Size is:', oRectangle1.getDimensions(), " area is:", oRectangle1.getArea())

# Create a rectangle of width 10 and length 2
oRectangle2 = Rectangle(10, 2, '-', '|', '*')
oRectangle2.show()
print('Size is:', oRectangle2.getDimensions(), " area is:", oRectangle2.getArea())

# Tell the first rectangle to modify its data
oRectangle1.setWidth(7)
oRectangle1.setLength(5)
oRectangle1.setHorizontalChar('^')
oRectangle1.setVerticalChar('?')
oRectangle1.setCornerChar('$')
oRectangle1.show()
print('Size is:', oRectangle1.getDimensions(), " area is:", oRectangle1.getArea())
print()


# In[ ]:





# In[ ]:





# In[ ]:




