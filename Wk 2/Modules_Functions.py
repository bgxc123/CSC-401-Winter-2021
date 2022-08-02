# Modules_Functions.py
# containers for Python code

##### previously #####
'''
Cast of characters and the operations and
expressions that manipulate them:

    bool, int, float, str, list

    =,+,-,**,==,<, ... 
'''

##### MODULE (== .py file) #####

'''
A MODULE is an executable Python file.
Our Python modules will consist mainly of
FUNCTION (and class) definitions.

Ctrl-s - save module
F5 - run module
'''

2+3 # calculated, but not displayed

print(2+3) # displayed!

# can also define things to be referred to
# later

z = 3*4

##### def - FUNCTION definition #####
'''
a FUNCTION is a package for statements.
It allows to decide when and where a
function will be CALLED/INVOKED (used).

basic version:

def <functionname>():
    <indented statements>
'''

def myFunction():
    x = 4*3
    print( x )

print('statement not in function')

'''
5
statement not in function
>>> # to call/invoke function
>>> myFunction()
12
>>> myFunction
<function myFunction at 0x000001EF355DC1E0>
>>>
'''

# NOTE: will postpone coverage of the
# input() function

##### PARAMETERS - INPUTS/local VARIABLES #####

'''
function with PARAMETERS:

def <functionname>(par0,par1,...):
    <indented statements>

par0, par1,...  are inputs to the function
and LOCAL VARIABLES that can be used
*ONLY* inside the function.
'''

# x=2, y=3 happens automatically
def function(x,y):
    print('x is',x)
    print('y is',y)

# print(x) # causes error, x is NOT visible

'''
>>> function()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    function()
TypeError: function() missing 2 required positional arguments: 'x' and 'y'
>>> function(2,3) # supply arguments
x is 2
y is 3
>>>
'''

##### RETURN vs. PRINT - function output #####
'''

A function can OUTPUT using either PRINT
or RETURN. Always read the problem
description CAREFULLY to find out which
you should use:

print - display information for user
      - output NOT usable by code

return - formal way of saying
         "the answer is"
       - answer is USABLE by other code
       - the function call/invocation
         has the value of the value
         that was RETURNED 

RETURN is generally PREFERRED.  But, the
code can be a bit trickier to write (see
ACCUMULATION coming soon.)
'''

##### RETURN #####

'''
Write a function celsius that accepts a
Fahrenheit temperature and RETURNS the
Celsius equivalent.

make this work:

>>> celsius(32.0)
0.0
>>> celsius(212.0)
100.0
>>> celsius(-40)
-40.0
>>> celsius(32) - 8.3 # windchill
-8.3
'''

#v1 - with PRINT
def celsius(f):
    ''' Given a Fahrenheit temperature f,
    return the Celsius equivalent'''
    c = (f-32)*5/9 # per Wikipedia ...
    print( c )

'''
mostly seems OK

>>> celsius(32)
0.0
>>> celsius(212)
100.0
>>> celsius(-40)
-40.0

BUT, output is NOT usable in subsequent
calculations (because we used print)

>>> celsius(32) - 8.3 # windchill
0.0
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    celsius(32) - 8.3 # windchill
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'
>>>
'''

#v1 - with PRINT
# NOTE: last function def sticks
def celsius(f):
    ''' Given a Fahrenheit temperature f,
    return the Celsius equivalent'''
    c = (f-32)*5/9 # per Wikipedia ...
    return c  # the answer is c

'''
>>> celsius(32)
0.0
>>> celsius(32) - 8.3 # windchill
-8.3
>>>
'''

##### DOCSTRING ######
'''
docstring - the first multiline comment
inside a function is accessible outside
the function through HELP and/or CODE
HINTS.

>>> help(celsius)
Help on function celsius in module __main__:

celsius(f)
    Given a Fahrenheit temperature f,
    return the Celsius equivalent

>>>
'''

















