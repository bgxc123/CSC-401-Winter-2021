# Tuples.py

##### tuple #####
'''
tuple
- (item, item, item, ...)
- () are sometimes optional
- like a list but IMMUTABLE
- can be used as dict keys
- can be used in sets

tuple assignment:

    tuple of variables = tuple of expressions

    for example:
    x,y,z = expr1,expr2,expr3

1) evaluate expressions
2) obtain tuple of values
3) assign values to variables

>>> t = (4,2,3)
>>> t
(4, 2, 3)
>>> type(t)
<class 'tuple'>
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> t[1]
2
>>> t[1] = 99
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t[1] = 99
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> x = 7
>>> # is x one of 2,3 or 5
>>> x==2 or x==3 or x==5
False
>>> # equivalent
>>> x in (2,3,5)
False
>>> 
>>> # tuple assignment
>>> a,b = 4,5
>>> a
4
>>> b
5
>>> x,y = 2*a, 3*b
>>> x
8
>>> y
15
>>> 
>>> # swapping values
>>> x
8
>>> y
15
>>> y = x
>>> x
8
>>> y
8
>>> x,y = 8,15
>>> # swap without tuple
>>> x = 8
>>> y = 15
>>> temp = x
>>> x = y
>>> y = temp
>>> x
15
>>> y
8
>>> # swap with tuple
>>> x,y = y,x
>>> x
8
>>> y
15
>>> 
'''

