# Exceptions.py

##### Exceptions #####
'''
An EXCEPTION is a message that is sent
when a run-time error occurs.

you can either:
1) CATCH and HANDLE with TRY/EXCEPT, or
2) execution will stop.

We can also:
1) RAISE exceptions, and
2) write CUSTOM EXCEPTION classes
'''

##### EXCEPTIONS/ERRORS #####

# lots of ways to cause exceptions/errors

'''
>>> open('doesnotexist.txt')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    open('doesnotexist.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'doesnotexist.txt'
>>> x
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> 3+"3"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    3+"3"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int("3")
3
>>> int("three")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("three")
ValueError: invalid literal for int() with base 10: 'three'
>>>
'''
##### CATCH and HANDLE with try/except #####
'''
try/except can be used to CATCH
and HANDLE exceptions.

try:
    code that may cause error
except:
# or except ErrorType:
    code that runs if error occurs

BUT, try/except can hide coding errors.
SO, narrow use by:

1) limit code in try block
2) list specific error types

>>> # try/except
>>> import random
>>> x = random.randrange(2) # 0 or 1
>>> try:
	print( 1/x )
except:
	print('x is zero')

	
1.0
>>> x
1
>>> x = random.randrange(2) # 0 or 1
>>> try:
	print( 1/x )
except:
	print('x is zero')

	
x is zero
>>> z
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> x
0
>>> 
>>> # can type error
>>> x
0
>>> try:
	print( 1/x )
except ZeroDivisionError:
	print('x is zero')

	
x is zero
>>> try:
	print( 1/x )
except ValueError:
	print('x is zero')

	
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    print( 1/x )
ZeroDivisionError: division by zero
>>> 
'''

##### RAISING ERRORS #####
'''
It is easy to raise errors as follows:

raise ErrorType('optional message')
>>> # raise errors
>>> raise ValueError()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    raise ValueError()
ValueError
>>> raise ValueError( "your message here")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    raise ValueError( "your message here")
ValueError: your message here
>>> 
'''

##### Custom Error class #####
'''
custom error classes are the easiest
classes you will write:

1) inherit from Exception
2) use implementation pass

Why?  A: can then raise, catch and handle
your CustomError.
'''

class CustomError(Exception): # inherit from Exception
    pass
    
'''
>>> raise CustomError()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    raise CustomError()
CustomError
>>> raise CustomError('my message here')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    raise CustomError('my message here')
CustomError: my message here
>>>
'''



