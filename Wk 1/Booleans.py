# Booleans.py

##### bool(ean) values/expressions ##### 

'''
bool(ean) value - numerical value of
either True or False

boolean expressions - math expressions
with a result of True/False

boolean operators:

    ==, != - equal, not equal
    <,<=,>,>= - less than, less than equal, ...

compounds operators:

    not, and, or 

conversions:

    from bool to int/float
    True->1, False->0

    reverse direction
    0->False, everything else-> True

    >>> # number types in Python
>>> type(9)
<class 'int'>
>>> type(-2.3)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 
>>> # checking equality
>>> x = 2
>>> # is x equal to 3?
>>> x == 3
False
>>> x==2
True
>>> 
>>> # not equals, other comparis
>>> # ons
>>> x!=3
True
>>> x!=2
False
>>> x<2 # strictly less
False
>>> x<=2
True
>>> x>3
False
>>> x>=3
False
>>> 
>>> # how to check if a number is odd
>>> x = 7
>>> x%2
1
>>> 6%2
0
>>> # test for odd
>>> x%2 != 0  # or x%2==1
True
>>> x = 8
>>> x%2 != 0  # or x%2==1
False
>>> # check whether a number is divisible
>>> # by 3
>>> x%3==0
False
>>> x=6
>>> x%3==0
True
>>> 
>>> # compound booleans with and/or
>>> 
>>> # check whether a number is divisible
>>> # by 2 or 3
>>> x%2==0 or x%3==0
True
>>> x
6
>>> x = 9
>>> x%2==0 or x%3==0
True
>>> 
>>> # not
>>> x = 5
>>> x<6
True
>>> not x<6 # negates result
False
>>> 
>>> # and
>>> x%2==0 and x%3==0
False
>>> x
5
>>> x=9
>>> x%2==0 and x%3==0
False
>>> x=12
>>> x%2==0 and x%3==0
True
>>> 
>>> 
>>> # pitfall
>>> # check whether x is one of 2,3, or 4
>>> x = 7
>>> x == 2 or 3 or 4
3
>>> # much better
>>> x==2 or x==3 or x==4
False
>>> x = 4
>>> x==2 or x==3 or x==4
True
>>> 
>>> 
>>> # conversions
>>> int(True)
1
>>> int(False)
0
>>> bool(1)
True
>>> bool(0)
False
>>> bool(.0001)
True
>>> 

'''

