# Point1.py - Part 1 of 2
# lab2 and hw1 will require both parts


##### IMPORTANT: sleight of hand #####
'''

The Python interpreter converts BOUND
method calls to UNBOUND method calls.

BOUND - OBJECT to the left:

    lst.append(5)

UNBOUND - CLASS to the left:

    list.append(lst,5)

So, in general, when you say:

    obj.method( arg1, arg2, ...)

Python determines obj's class, say
MyClass, and then executes the following

    MyClass.method( obj, arg1, arg2, ...)

>>> lst = [2,3,4]
>>> lst.append(5)
>>> lst
[2, 3, 4, 5]
>>> list.append(lst,5)
>>> lst
[2, 3, 4, 5, 5]
>>> 
>>> s = 'apple'
>>> s.upper()
'APPLE'
>>> type(s)
<class 'str'>
>>> str.upper(s)
'APPLE'
>>> 
'''

##### goal #####
'''
make this work:

>>> p = Point() # constrSuctor
>>> p.setx( 4 )
>>> p.sety( 7.1 )
>>> p.get()
(4, 7.1)
>>> p.move(1,1) # relative move
>>> p.get()
(5, 8.1)
... more stuff later ...
'''
##### Point - v1 - all methods explicit #####

# create the class
class Point:

    # method - function inside the class
    # p.setx(4) -> Point.setx(p,4)
    def setx(self,xcoord): # self is calling object, p in this case
        self.x = xcoord # x is an ATTRIBUTE of self
    def sety(self,ycoord):
        self.y = ycoord
    # p.get() -> Point.get(p)
    def get(self):
        return (self.x,self.y)
    def move(self,deltax,deltay):
        self.x = self.x + deltax
        self.y = self.y + deltay
        '''
        self.x += deltax
        self.y += deltay
        '''
'''
>>> p = Point()
>>> p.setx(4)
>>> p.sety(3.1)
>>> p.get()
(4, 3.1)
>>> p.move(-1,1)
>>> p.get()
(3, 4.1)
>>>
'''

##### BUT - there is a problem #####

'''
If we access a data attribute before it is
created, ERROR!

>>> p = Point()
>>> p.setx(4)
>>> p.get()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    p.get()
  File "C:/Users/esedgwic/Dropbox/courses/csc242/lectures/Point1.py", line 73, in get
    return (self.x,self.y)
AttributeError: 'Point' object has no attribute 'y'
>>> vars(p)
{'x': 4}   # no y!
'''

# MORE stuff in Part 2
# magic/dunder method
# Point client












        










