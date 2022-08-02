# Point2.py - Part 2 of 2
# lab2 and hw1 will require both parts

# MAGIC/DUNDER methods
# Point CLIENT

##### Point - v2 - MAGIC/DUNDER methods #####

class Point:

    # constructor/__init__
    # p = Point(2,3) -> Point.__init__(p,2,3)
    # =0 are DEFAULT ARGUMENTS that are
    # used if arguments are not provided
    def __init__(self,xcoord=0,ycoord=0):
        #print('__init__')
        self.x = xcoord
        self.y = ycoord

    # repr is called automatically when
    # a str representation is needed
    def __repr__(self):
        return f"Point({self.x},{self.y})"
        return "Point({},{}".format(self.x,self.y)

    # p==q -> Point.__eq__(p,q)
    # RETURN a bool!
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y: # the same
            return True
        else:
            return False
        # or, more succintly
        return self.x==other.x and self.y==other.y       
    
    # p.setx(4) -> Point.setx(p,4)
    def setx(self,xcoord): # self is calling object, p in this case
        self.x = xcoord # x is an ATTRIBUTE of self
    def sety(self,ycoord):
        self.y = ycoord
    # p.get() -> Point.get(p)
    def get(self):
        return (self.x,self.y)
    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
##### MAGIC/DUNDER methods #####
'''
MAGIC/DUNDER methods are called
automatically by the Python interpreter
(without being explicitly called by name).

names are FIXED, you MUST name them
exactly (otherwise they wont execute)

__init__ - the constructor, called when an
object is created, INITIALIZES/MODIFIES
the object (adds attributes to self)

__repr__ - RETURNS a str version of the
object when one is needed (printing, str,
repr, IDLE)

__eq__ is ==

many more ... can look them up : + - __add__, < - __lt__
'''

##### movePointAround - Point CLIENT #####

'''
want this to work:
>>> p = movePointAround()
Enter a point: 1,2
Point(1,2)
Move it how? 1,1
Point(2,3)
Move it how? 5,-5
Point(7,-2)
Move it how?
>>> p
Point(7,-2)
'''

# movePointAround is a Point CLIENT
# uses services of Point class
# but is NOT part of (inside) the Point class

def movePointAround():

    x,y = eval( input('Enter a point: '))
    pt = Point(x,y)
    while True:
        ans = input('Move it how? ')
        if ans == '':
            break
        else: # move the point!
            dx,dy = eval(ans)
            pt.move(dx,dy)
            print( pt )
    # dont convert to a str
    return pt
            

# using eval and tuple assignment
'''
>>> ans = "1,1\n"
>>> ans
'1,1\n'
>>> eval(ans) # produces tuple
(1, 1)
>>> # tuple assignment
>>> x,y = (3,4)
>>> x
3
>>> y
4
>>> ans
'1,1\n'
>>> x,y = eval(ans)
>>> x,y
(1, 1)
>>>
'''
    

##### ==/is #####
'''
generally we expect:

== - compares the CONTENTS of objects, do
two objects have the same value?

is - compares MEMORY LOCATION of objects,
are two objects the same (in memory)

BUT, if you dont write ==/__eq__, Python
checks MEMORY LOCATIONS (uses is)

so if you NEED ==, make sure you write
__eq__

>>> # == vs is
>>> lst = [1,2]
>>> lst2 = [1,2]
>>> lst == lst2
True
>>> lst is lst2
False
>>> id(lst), id(lst2)
(2440175090824, 2440175089096)
>>> 
>>> lst = [1,2]
>>> lst2 = lst
>>> lst == lst2
True
>>> lst is lst2
True
>>> id(lst), id(lst2)
(2440177339144, 2440177339144)
>>>
'''









































