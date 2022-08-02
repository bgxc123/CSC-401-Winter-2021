# Sets.py

##### set #####

'''
set is a Python implementation of a
mathematical set (discrete math?):

    a collection, like a list BUT
    
    items unique (no duplicates)

    unordered

    efficient! (uses hash functions)

creating sets - DELIMIT with {}

    {item, item, item, ...}

    set() - for empty set

modifying set:

    add(item)

    remove(item) - causes error if item
    not in set

    discard(item) - does not cause error
    if item not in set

    update( iterable) - adds each item in
    iterable to set (iterated add)

    union, intersection 

operators:

    in, not in - containment/iteration

    & - intersection

    | - union


Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # DELIMIT a set with {}
>>> s = {2,3,4,6}
>>> s
{2, 3, 4, 6}
>>> s.add(99)
>>> s
{2, 99, 3, 4, 6}
>>> s.add(3)
>>> s
{2, 99, 3, 4, 6}
>>> s.add( [1,2] )
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.add( [1,2] )
TypeError: unhashable type: 'list'
>>> s.add( (1,2) )
>>> s
{(1, 2), 2, 99, 3, 4, 6}
>>> s.remove(2)
>>> s
{(1, 2), 99, 3, 4, 6}
>>> s.remove(2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.remove(2)
KeyError: 2
>>> s.discard(2) # no error if not there
>>> 
>>> # operators
>>> s
{(1, 2), 99, 3, 4, 6}
>>> 4 in s
True
>>> 4 not in s
False
>>> for item in s:
	print(item)

	
(1, 2)
99
3
4
6
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s[1]
TypeError: 'set' object does not support indexing
>>> 
>>> # to create an empty set
>>> # note, this wont work
>>> s = {}
>>> s.add(3)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s.add(3)
AttributeError: 'dict' object has no attribute 'add'
>>> # do this instead
>>> s = set()
>>> s.add(3)
>>> s
{3}
>>> type(s)
<class 'set'>
>>> set( [4,1,0,2,1,1,4] )
{0, 1, 2, 4}
>>> set( 'apple' )
{'a', 'e', 'p', 'l'}
>>> 
>>> # update method
>>> s = {2,3,4}
>>> s.update( {5,1,2} )
>>> s
{1, 2, 3, 4, 5}
>>> # union/intersection - &/|
>>> {2,3,5,6} & {6,2,9,7} # intersection
{2, 6}
>>> {2,3,5,6} | {6,2,9,7} # union
{2, 3, 5, 6, 7, 9}
>>> 

'''

































>>> # set
>>> # also uses curly braces!
>>> s = {2,3,4,6}
>>> s
{2, 3, 4, 6}
>>> s.add( 99 )
>>> s
{2, 99, 3, 4, 6}
>>> s.add( 3 )
>>> s
{2, 99, 3, 4, 6}
>>> # no duplicates!
>>> s.add( 3 )
>>> s
{2, 99, 3, 4, 6}

# items must be immutable (hashable)
>>> s.add( [2,3] )
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.add( [2,3] )
TypeError: unhashable type: 'list'
>>> s.add( (2,3) )
>>> s
{2, 99, 3, 4, 6, (2, 3)}
>>>

# remove
>>> s.remove(3)
>>> s
{2, 99, 4, 6, (2, 3)}
>>> s.remove(3)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.remove(3)
KeyError: 3
>>> # remove raises error if item not there
>>> s.discard( 4 )
>>> s
{2, 99, 6, (2, 3)}
>>> s.discard( 4 )
>>> # discard doesnt cause error


# operators

#in

>>> 4 in s
False
>>> 6 in s
True
#not in

#in - also for iteration

>>> for item in s:
	print(item)

	
2
99
6
(2, 3)
>>> s
{2, 99, 6, (2, 3)}

# but cant index!
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable

 
>>> # to create empty set

# this doesnt work
>>> s = {}
>>> s.add( 3 )
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.add( 3 )
AttributeError: 'dict' object has no attribute 'add'
>>> type(s)
<class 'dict'>

# instead do this
>>> # whoops, must call constructor
>>> # explicitly
>>> s = set()
>>>

# convert to set

set([4,1,0,2,1,1,4]

set('apple')



# update

s = {2,6,7}

s.update( {5,7} )

s.update(  )

# &/|

>>> {2,3} & {3,4}
{3}
>>> {2,3} | {3,4}
{2, 3, 4}
>>> 



    


