#!/usr/bin/env python
# coding: utf-8

# In[30]:


print('''
      
In Python, access control for class methods (private, public, protected) is achieved through naming conventions rather than enforced restrictions. 
The standard Python libraries that help define public and private methods include:

1. Built-in Naming Conventions (No Additional Library Needed)

Python does not have strict private/public access modifiers like C++ or Java. Instead, it uses naming conventions:

Public Methods: No underscore prefix (e.g., def my_method(self):).
Protected Methods: Single underscore _my_method(self), indicating it’s intended for internal use but not enforced.
Private Methods: Double underscore __my_method(self), which triggers name mangling.

''')


# In[31]:


class MyClass:
    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method (by convention)")

    def __private_method(self):
        print("This is a private method (name mangled)")

    def access_private(self):
        self.__private_method()  # Allowed within class

obj = MyClass()
obj.public_method()       # ✅ Accessible
obj._protected_method()   # ✅ Accessible (but discouraged)
# obj.__private_method()  # ❌ AttributeError
obj.access_private()      # ✅ Works, as it calls private method inside class

# 👉 Name mangling: The actual method name becomes _MyClass__private_method, preventing accidental access but still accessible if needed 
# (obj._MyClass__private_method()).


# In[33]:


print("Using a library - accessify - to set up the public and the private methods") 


# In[34]:


print('''
@public makes it explicit that the method is accessible.
@private prevents external access but allows internal use.
''')


# In[2]:


print('''An example given by GPT4:

pip install pyaccess

from pyaccess import private, public

class Example:
    @public
    def public_method(self):
        """This method is accessible anywhere"""
        print("Public method called")

    @private
    def private_method(self):
        """This method is only accessible within the class"""
        print("Private method called")

    def access_private(self):
        self.private_method()  # Allowed within the class

obj = Example()

obj.public_method()  # ✅ Works
# obj.private_method()  # ❌ Raises AttributeError
obj.access_private()  # ✅ Works, accessed internally

''')


# In[35]:


from accessify import private, protected

class Example:
    @private
    def __private_method(self):
        print("Private method called")

    @protected
    def _protected_method(self):
        print("Protected method called")

    def access_private(self):
        self.__private_method()  # Allowed within the class

obj = Example()

# obj.__private_method()  # ❌ Raises AttributeError
obj.access_private()  # ✅ Works

# obj._protected_method()  # ❌ Raises AttributeError


# In[55]:


print('''More examples :

Key Takeaways:

@public is unnecessary because methods are public by default.
@protected methods can be accessed inside the class or by subclasses.
@private methods can only be accessed inside the class

''')


# In[37]:


from accessify import private, protected

class Example:
    def public_method(self):
        """This is a fully accessible public method"""
        print("Public method called")

    @protected
    def _protected_method(self):
        """This method is accessible only inside the class and subclasses"""
        print("Protected method called")

    @private
    def __private_method(self):
        """This method is strictly private"""
        print("Private method called")

    def access_private(self):
        """Access private method internally"""
        self.__private_method()  # ✅ Allowed inside the class

    def access_protected(self):
        """Access protected method internally"""
        self._protected_method()  # ✅ Allowed inside the class

obj = Example()

# Public method (accessible)
obj.public_method()  # ✅ Works

# Protected method (raises an error if accessed externally)
# obj._protected_method()  # ❌ Raises AttributeError

# Private method (raises an error if accessed externally)
# obj.__private_method()  # ❌ Raises AttributeError

# Internal calls
obj.access_private()  # ✅ Works (internal access allowed)
obj.access_protected()  # ✅ Works (internal access allowed)


# In[56]:


print('''

Using Python’s Built-in Convention (_protected, __private).

If you don’t want external dependencies, use Python’s naming conventions.

Key Takeaways
_protected_method() is a convention but not enforced.
__private_method() is name-mangled, so it’s harder to access externally.

Direct access to private methods via _Example__private_method() is possible but discouraged.
''')


# In[57]:


class Example:
    def public_method(self):
        """This is a public method"""
        print("Public method called")

    def _protected_method(self):
        """This is a protected method (by convention)"""
        print("Protected method called")

    def __private_method(self):
        """This is a private method (name mangled)"""
        print("Private method called")

    def access_private(self):
        """Access private method internally"""
        self.__private_method()  # ✅ Works inside the class

    def access_protected(self):
        """Access protected method internally"""
        self._protected_method()  # ✅ Works inside the class

obj = Example()

obj.public_method()  # ✅ Works
obj._protected_method()  # ✅ Works (but discouraged)
# obj.__private_method()  # ❌ Raises AttributeError
obj.access_protected()  # ✅ Works (internal access allowed)
obj.access_private()  # ✅ Works (internal access allowed)

# Name mangling workaround (not recommended)
obj._Example__private_method()  # ✅ Works, but should be avoided


# In[ ]:





# In[41]:


print('''About Metaclasses :

What is a Metaclass in Python?
A metaclass is a special kind of class that defines how other classes behave. In other words, a metaclass is a class for classes.

Key Concept
In Python, everything is an object, including classes.

A class is an instance of a metaclass (just like an object is an instance of a class).
By default, Python classes are created using type, which is the built-in metaclass.
Metaclasses allow modifying class behavior at creation time.

''')


# In[43]:


print(''' About Abstract Classes :

An abstract class method is a method that is declared but contains no implementation. 
It is used as a template for other methods that are defined in a subclass.

''')


# In[44]:


print("https://www.tutorialsteacher.com/python/public-private-protected-modifiers")


# In[45]:


# Example: Public AttributesCopy
class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

# You can access the Student class's attributes and also modify their values, as shown below.
# Example: Access Public MembersCopy

std = Student("Steve", 25)
print(std.schoolName)  #'XYZ School'
print(std.name)  #'Steve'
std.age = 20
print(std.age)


# In[46]:


print('''

Protected members of a class are accessible from within the class and are also available to its sub-classes. 
No other environment is permitted access to it. This enables specific resources of the parent class to be inherited by the child class.

Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. 
This effectively prevents it from being accessed unless it is from within a sub-class.

''')

# Example: Protected AttributesCopy
class Student:
    _schoolName = 'XYZ School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute

# In fact, this doesn't prevent instance variables from accessing or modifying the instance. 
# You can still perform the following operations:

# Example: Access Protected Members Copy

std = Student("Swati", 25)
print(std._name)  #'Swati'

std._name = 'Dipa'
print(std._name)  #'Dipa


# In[47]:


# However, you can define a property using property decorator and make it protected, as shown below.
# Example: Protected AttributesCopy

class Student:
	def __init__(self,name):
		self._name = name
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,newname):
		self._name = newname

# Above, @property decorator is used to make the name() method as property and @name.setter decorator to another overloads of the name() method 
# as property setter method. Now, _name is protected.

# Example: Access Protected MembersCopy

std = Student("Swati")
print(std.name)  #'Swati'

std.name = 'Dipa'
print(std.name)  #'Dipa'
print(std._name) #'Dipa'


# In[ ]:





# In[49]:


print('''Private Members :

Python doesn't have any mechanism that effectively restricts access to any instance variable or method. 
Python prescribes a convention of prefixing the name of the variable/method with a single or double underscore 
to emulate the behavior of protected and private access specifiers.

The double underscore __ prefixed to a variable makes it private. 
It gives a strong suggestion not to touch it from outside the class. 
Any attempt to do so will result in an AttributeError.
''')

# Example: Private AttributesCopy

class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')

std = Student("Bill", 25)
# print(std.__schoolName)  #AttributeError
# print(std.__name)        #AttributeError
# print(std.__display())   #AttributeError

print('''
Python performs name mangling of private variables. 
Every member with a double underscore will be changed to _object._class__variable. 
So, it can still be accessed from outside the class, but the practice should be refrained.
''')

# Example: Access Private VariablesCopy
std = Student("Bill", 25)
print(std._Student__name)  #'Bill'

std._Student__name = 'Steve'
print(std._Student__name)  #'Steve'
std._Student__display()    #'This is private method.'


# In[50]:


print('''
Method Overloading:

Method overloading is a feature in Python that allows a class to have multiple methods with the same name but with different parameters. 
This feature helps to provide flexibility and reusability to the code design. 
It is different from method overriding that allows a subclass to provide its implementation of a method defined in its superclass.

''')


# In[51]:


print('''
Python Getter and Setter Methods

Python offers getter and setter convenience methods to control access to the private instance variables for classes. 

The getter and setter methods are important because without them, 
the private instance variables would not be accessible outside of the class.

Getter method allows to access the value of a private instance variable from outside a class, 
and the setter method allows to set the value of a private instance variable from outside a class.

''')


# In[52]:


class MyClass:
    def __init__(self):
        self._value = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

obj = MyClass()
obj.set_value(10)
print(obj.get_value())


# In[53]:


class MyClass:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

obj = MyClass()
obj.value = 10
print(obj.value)


# In[ ]:


print(''''
Method overriding : 
It is a feature in object-oriented programming that allows a subclass to provide a different implementation of a method that is already 
defined in its superclass. In Python, method overriding is straightforward and is achieved by defining a method in the subclass with 
the same name as the method in the superclass.
''')


# In[54]:


class Animal:
  def move(self):
    print("Animal is moving")

class Bird(Animal):
  def move(self):
    super().move()
    print("Bird is flying")

obj = Bird()
obj.move() ### prints "Animal is moving" and "Bird is flying


# In[ ]:




