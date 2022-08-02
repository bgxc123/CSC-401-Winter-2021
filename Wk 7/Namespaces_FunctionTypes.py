# Namespaces_FunctionTypes.py

##### NOTES: #####
'''
dict(ionaries) are needed for this
discussion.  Please review if neccesary.

presentation a bit different than the
textbook, especially use of vars()
'''

##### namespaces, vars() #####

'''
vars() - returns namespace "handy dandy
notebook"

function that returns current namespace,
i.e., a dictionary with variables and the
objects they refer to.

Python follows the LEGB rule for looking
up variables (SCOPE).  Variables are
looked up in the following order:

1) L(ocal) function: x
2) E(nclosing)* function: N/A*
3) G(lobal)/Module: y
4) B(uiltins): print, abs

* Don't worry about 2), this only applies
for nested functions, which you may not
have seen yet.
'''

##### import #####

'''
import modifies current namespace, vars()

import math - adds math module to current
namespace

from math import pi - adds pi to current
namespace

from math import * - adds everything to
current namepace (pollutes namespace, can
lead to name COLLISIONS which is bad)

'''


##### 3 types of functions/methods #####

'''
functions: abs(), max(), len()

methods: a method is a function that is
defined inside a class: list.append,
str.upper.

3 Types:

1)function/method that MODIFIES something.
NOT USABLE in an expression or assignment
statement.

   list.append
   list.sort
   print
   

2) function/method that RETURNS something
USABLE in an expression or assignment
statement
       
   abs, max, len
   str.upper
   sorted
   
3) function/method that MODIFIES and
RETURNS

   list.pop
   input

>>> # how does Python store variables?
>>> x=77
>>> 2*x
154
>>> 2*y # y not assigned yet
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    2*y # y not assigned yet
NameError: name 'y' is not defined
>>> # vars() - handy dandy notebook
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 77}
>>> vars()['y'] = 100
>>> 2*y
200
>>> # many namespaces
>>> # scope: LEGB
>>> 
>>> x = 2
>>> y = 3
>>> def f():
	x = 99
	print(x,y)
	print( vars() )

	
>>> f() # what is the output?
99 3
{'x': 99}
>>> len( vars(__builtins__))
154
>>> 'print' in vars(__builtins__)
True
>>> 'abs' in vars(__builtins__)
True
>>> 
>>> 
>>> # Python lets us mess things up!
>>> abs(-5)
5
>>> def g(x):
	return 0

>>> abs = g
>>> abs(-5)
0
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 2, 'y': 3, 'f': <function f at 0x000002865D4AC1E0>, 'g': <function g at 0x000002865FA80D90>, 'abs': <function g at 0x000002865FA80D90>}
>>> 
>>> vars().pop('abs')
<function g at 0x000002865FA80D90>
>>> abs(-5)
5
>>> 
>>> # import modifies namespaces
>>> # want to use pi
>>> import math
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 2, 'y': 3, 'f': <function f at 0x000002865D4AC1E0>, 'g': <function g at 0x000002865FA80D90>, 'math': <module 'math' (built-in)>}
>>> math
<module 'math' (built-in)>
>>> math.pi
3.141592653589793
>>> math.cos
<built-in function cos>
>>> from math import pi
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 2, 'y': 3, 'f': <function f at 0x000002865D4AC1E0>, 'g': <function g at 0x000002865FA80D90>, 'math': <module 'math' (built-in)>, 'pi': 3.141592653589793}
>>> pi
3.141592653589793
>>> len( vars() )
13
>>> from math import *
>>> len( vars() )
62
>>> 
>>> 
>>> # 3 types function/methods
>>> 
>>> lst = [3,1,2,7]
>>> lst.append(6)
>>> lst2 = lst.sort()
>>> lst2
>>> lst
[1, 2, 3, 6, 7]
>>> 
>>> lst
[1, 2, 3, 6, 7]
>>> lst = [3,1,2,7]
>>> sorted( lst )
[1, 2, 3, 7]
>>> lst
[3, 1, 2, 7]
>>> lst2 = sorted( lst )
>>> lst
[3, 1, 2, 7]
>>> lst2
[1, 2, 3, 7]
>>> 
>>> lst.pop()
7
>>> lst
[3, 1, 2]
>>> item = lst.pop()
>>> lst
[3, 1]
>>> item
2
>>> x = print(5)
5
>>> x
>>> ans = input('enter a number: ')
enter a number: 23
>>> ans
'23'
>>> 
>>> s = 'apple'
>>> s.upper()
'APPLE'
>>> s = s.upper()
>>> s
'APPLE'
>>> 
>>> len( lst )
2
>>> 

'''
