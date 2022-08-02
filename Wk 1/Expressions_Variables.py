# Expressions_Variables.py

##### expressions #####
'''

We can use IDLE like a calculator by
typing EXPRESSIONS in the shell (or file).
We can use these mathematical operators
(listed in order of precedence):

    ()
    **
    *,/,//,%
    +,-

    // - floor division, also called "div"
    %  - remainder, modulus or "mod"

We can also use functions, for example:

    max, min
    abs

>>> 2+3
5
>>> 2-3
-1
>>> 3*3.3
9.899999999999999
>>> 4**3
64
>>> 2+3*5
17
>>> (2+3)*5
25
>>> 3**.5
1.7320508075688772
>>> 24/5
4.8
>>> 
>>> # div/mod
>>> 23//5
4
>>> 23%5
3
>>> # very useful
>>> # 132 minutes in hours and minutes
>>> 132//60
2
>>> 132%60
12
>>> # functions
>>> abs(-5)
5
>>> max(-2,-3)
-2
>>> max(2,3,4,-99,78.3)
78.3
>>> 
>>> # convert 32 degrees fahrenheit
>>> # to celsius
>>> 32 - 32 * 5/9
14.222222222222221
>>> (32 - 32) * 5/9
0.0
>>> 
'''

##### variables #####

'''
Variables are names for objects/values
give us a way to remember things.

Variables are created with assignment
statements:

<variable> = <expression>

1) <expression> is computed
2) result is stored with name <variable>

variables:
    - dont exist until they are assigned to
    - can be reused/reassigned
    - dont care what type they hold
      (but expressions do care!)

variables names
    - use a..z, A..Z, 0..9, _
    - cant start with digit
    - names are cAsE SenSiTIVE,
      fred not the same as fRed
    - use meaningful names that are not too
      long
    - use camelCase, JoeTheRobot
    - or Joe_the_robot
    - dont use keywords or
      core language (or builtins!)

vars() - shows the variables that are
available in the current namespace
(context)

>>> # variables
>>> 2+3
5
>>> x = 2+3 # assignment statement
>>> x
5
>>> x*6.1
30.5
>>> y
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> y = x**2
>>> y
25
>>> 
>>> # vars()
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '

'''

