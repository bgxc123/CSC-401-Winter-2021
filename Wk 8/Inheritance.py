# Inheritance.py



##### inheritance #####
'''
INHERITANCE - customize/modify an existing
class instead of building from scratch.

terminology:
- INHERITED=SUB=CHILD class
- BASE=SUPER=PARENT class
    
An OBJECT of the subclass is also an
INSTANCE of, and has the METHODS of, the
super class.

Look for METHODS in this order:
1) subclass
2) super class

subclass has 4 types of METHODS:

0) INHERITED: DONT write, use super method
1) OVERRIDDEN: REPLACE super's method
2) ADDED: NEW method
3) EXTENDED - MODIFY super's method
'''

##### inheritance example #####
'''
note that the list repr puts
spaces between items

>>> # list repr
>>> lst = list(range(10))
>>> lst
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <- spaces between items
>>>

Let's eliminate the spaces! But, we dont
want to rewrite the whole class.  So we
will INHERIT from (SUBCLASS) list.
'''

# v1 - simplest example, NO NEW functionality
class MyList(list): # subclass/inherit from list
    pass

'''
>>> m = MyList()
>>> type(m)
<class '__main__.MyList'>
>>> m.append(2)
>>> m.append(3)
>>> m.append(4)
>>> m
[2, 3, 4]
>>> m.pop()
4
>>> m[1]
3
>>> type(m)
<class '__main__.MyList'>
>>> isinstance(m,MyList)
True
>>> isinstance(m,list)
True
>>>

1) TYPE of m is MyList
2) m is also an INSTANCE of the MyList class

EXAMPLE: Tiger is a subclass of Feline.
Every Tiger is an instance of Feline, but
not all Felines are Tigers.
'''

# v1 -with modificactijons
# inheritance: self IS a list INSTANCE
class MyList(list): # subclass/inherit from list
    # INHERIT: append, pop, ...

    # OVERRIDE repr
    def __repr__(self):
        # accumulate a str (without spaces)
        ans = "["
        for item in self: # no .attribute
            ans += repr(item) + ","
        return ans[:-1] + "]"

    # ADDED method
    def apply(self,function):
        for i in range(len(self)):
            self[i] = function( self[i] )

    # EXTEND coming soon ...
    # (usually repr)


    























