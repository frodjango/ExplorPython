# coding=utf-8


"""
https://www.programiz.com/python-programming/set

A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).

However, the set itself is mutable. We can add or remove items from it.
"""


"""
Function	Description

all()	    Return True if all elements of the set are true (or if the set is empty).
any()	    Return True if any element of the set is true. If the set is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of set as a pair.
len()	    Return the length (the number of items) in the set.
max()	    Return the largest item in the set.
min()	    Return the smallest item in the set.
sorted()	Return a new sorted list from elements in the set(does not sort the set itself).
sum()	    Return the sum of all elements in the set.

"""

a = set()
a.add(1)
a.add(2)
print a

b = {1, 2}
print b

if a == b:
    print "equivalent: {} vs {}".format(a, b)

x, y = b