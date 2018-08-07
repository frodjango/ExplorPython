# coding=utf-8
#---------------------
# Elagant classing...|
# --------------------

# Git version August 2018

# noinspection PyByteLiteral

"""
Built-In Class Attributes
=========================

Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other
attribute.

__dict__    Dictionary containing the class's namespace.

__doc__     Class documentation string or none, if undefined.

__name__    Class name.

__module__  Module name in which the class is defined. This attribute is "__main__" in interactive mode.

__bases__   A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.




Some extra function that works on objects
=========================================

Instead of using the normal statements to access attributes, you can use the following functions −

The getattr(obj, name[, default]) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.

exemples
--------

In [63]: getattr(fido, 'name')
Out[63]: 'fido'


getattr(fido, 'toto', 'defaut')
Out[67]: 'defaut'

In [68]: hasattr(fido, 'toto')
Out[68]: False

In [70]: delattr(fido, 'name')      # won't work on property like color or age
In [74]: delattr(fido, '_color')    # public variable so ok

"""

# ======================================================================================================================

class Dog(object):
    """
    Study of classes in python
    """

    # Class variables

    kind = 'canine'         # RW class variable shared by all instances
    __akind = 'canine private'     # invisible
    _akind = 'canine2'      # visible
    akind = 'canine3'       # visible

    # Class method - plus cool avec decorator

    @classmethod            # recent style using decorator
    def the_kind(cls):
        return cls.__akind


    @classmethod   # factory method
    def fromDalmatien(cls, name, age):
        """factory method"""
        return cls(name, age, 'blanc et noir')

    # Utility methods

    def __repr__(self):
        """
        Useful in interactive shell when typing a variable name
        """
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        """
        Overrides __repr__ if present for print statements
        """
        return "Dog:  name:{} age:{} color:{}".format(self.name, self.age, self.color)

    # Getter and setter experiments

    def __get_age(self):
        print("getter age")
        return self.__age       # private variable

    def __set_age(self, age):
        print("setter age")
        self.__age = age

    age = property(__get_age, __set_age)  # trick on getter and setter

    def __get_color(self):
        print("getter color")
        return self._color      # public variable

    def __set_color(self, color):
        print("setter color")
        self._color = color

    color = property(__get_color, __set_color)  # trick on getter and setter

    # Constructor

    def __init__(self, name, age, color):
        self.name = name    # instance variable unique to each instance
        self.age = age      # private variable
        self.color = color
        print "done constructing"
    # Simple method

    def majuscule_name(self):
        return self.name.upper()


fido = Dog('fido', 11, 'white')
print fido

toto = Dog.fromDalmatien('toto', 1)
print toto

print "------------------------------------"

# =====================================================================================================================

# Exemple de sous classes avec __init__ approprie

class Super(object):
    def __init__(self, x):
        self.x = x

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        self.y = y

s = Sub(1, 2)
print s.x, s.y #1 2

print "------------------------------------"

# =====================================================================================================================


class Animal(object):
    def talk(self):

        self.delegate_talking()

class Vache(Animal):
    def delegate_talking(self):
        print("meuh")

class Chevre(Animal):
    def delegate_talking(self):
        print("beeh")

class Fish(Animal):
    """ Overidden method"""
    def talk(self):
        Animal.talk(self)
        print "with bubbles"

    def delegate_talking(self):
        print("....")

c = Chevre()
v = Vache()
c.talk()
v.talk()

f = Fish()
f.talk()
