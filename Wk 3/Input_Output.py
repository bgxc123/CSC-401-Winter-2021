# Input_Output.py

##### I/O - input/output #####
'''
I/O functions:

    - print
    - input
    - eval

IMPORTANT: all I/O is done via strings!

NOTE: print/input are for communicating
with a USER. we will NOT use them as much
as you think!
'''

##### print #####
'''
print displays information to a USER.

print(arg1,arg2, ..., sep=' ',end='\n')

    - print none or more items
    - sep and end are OPTIONAL arguments
    - sep defaults to ' '
    - end defaults to '\n'

>>> # print
>>> print(2)
2
>>> print(2,3,'apple')
2 3 apple
>>> # sep
>>> print(2,3,'apple',sep='<->')
2<->3<->apple
>>> print(2,3,'apple',sep='')
23apple
>>> 
>>> # end
>>> for i in range(3):
	print(i)

	
0
1
2
>>> for i in range(3):
	print(i,end='-')

	
0-1-2-
>>> # both
>>> for i in range(3):
	print(2,3,'apple',sep='',end='')

	
23apple23apple23apple
>>> 
>>> # dont need to print anything
>>> print()

>>> print(2 +'apple')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(2 +'apple')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print( str(2) +'apple')
2apple
>>> 
'''

##### input #####
'''
input receives information from USER

variable = input('displayed message')

    - prints a message
    - prompts user for response
    - RETURNS user response, as a STR!
    - almost always assign to a variable

'''

#v1 - BAD
def inputTest(): # NO parameters, will get input from USER
    n = input('Enter a number:')
    print('your number is',n)
    print('twice your number is',2*n)

# input returns a STR
# n is a str!
'''
>>> inputTest()
Enter a number:234
your number is 234
twice your number is 234234
>>>
'''

#v2 - BETTER
def inputTest(): # NO parameters, will get input from USER
    n = eval( input('Enter a number:') )
    print('your number is',n)
    print('twice your number is',2*n)

'''
>>> inputTest()
Enter a number:234
your number is 234
twice your number is 468

>>> inputTest()
Enter a number:23.4
your number is 23.4
twice your number is 46.8
>>> 
>>> 
>>> # get input from USER
>>> inputTest(234)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    inputTest(234)
TypeError: inputTest() takes 0 positional arguments but 1 was given
>>>
'''

##### eval #####
'''
eval
    - converts a str to a number
    - does a lot more, probably TOO much
    - security issue for untrusted strings
    - can also use int,float
    - MOST class code uses eval


>>> # converting str's to number
>>> # int/float
>>> int('5')
5
>>> float('5')
5.0
>>> float('5.1')
5.1
>>> int('5.1')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int('5.1')
ValueError: invalid literal for int() with base 10: '5.1'
>>> 
>>> # eval is smarter
>>> eval('5')
5
>>> eval('5.0')
5.0
>>> x = 7
>>> # eval powerful, TOO powerful
>>> eval('2*x')
14
>>>   

'''













