# ProblemSolving.py

##### Cast of Characters ######

# bool, int, float - numbers
# str - sequence of characters
# list - sequence of items
# range - sequence of ints

##### Control Structures ######

# def - function definition
# if/(elif)/(else) - conditionals
# for loop - iteration

##### Problem Solving #####

# READ problem, EXAMINE sample usage

# before coding THINK/ASK QUESTIONS:

    # do you understand problem statement?
    # can you determine output?
    # solve the problem BY HAND
    # which techniques do you need?
    # do you need to reformat input?

# top-down design
# bottom-up implementation

##### say() #####

'''
write a function say that accepts two
arguments, a word (str) and an integer n.
the function then prints the word n
times.

want this to work:
>>> say('hello',3)
hello
hello
hello
>>> say('bye',2)
bye
bye
>>> say('ohmygosh!',0)
>>>
'''

def say(word,n):
    ''' prints word n times'''
    # repeat n times
    for i in range(n):
        print( word )
'''
>>> say('hello',3)
hello
hello
hello
>>> say('bye',2)
bye
bye
>>> say('ohmygosh!',0)
>>> range(0)
range(0, 0)
>>> len( range(0))
0
>>> list( range(0))
[]
>>>
'''

##### max #####
'''
max - write a function max that accepts
two numbers and returns the larger one

make this work:
>>> max(2,3)
3
>>> 4* max(2,3)
12
'''

# v1 - BAD, answer cant be used
# in expressions
def max(num1,num2):
    ''' returns the larger of num1 and num2'''
    if num1>=num2:
        print(num1)
    else:
        print(num2)

'''
>>> max(2,3)
3
>>> 4* max(2,3)
3
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    4* max(2,3)
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>>
'''

# v2 - GOOD, returns! (not print)
def max(num1,num2):
    ''' returns the larger of num1 and num2'''
    if num1>=num2:
        return num1
    else:
        return num2
'''
>>> max(2,3)
3
>>> 4* max(2,3)
12
>>>
'''


###### vowelStart #####

'''
make this work:  print the words in a list
that start with vowels

>>> lst = ['apple','hello','pear','orange']
>>> vowelStart( lst )
apple
orange
'''

def vowelStart( wordlst ):
    ''' print those words in wordlst that
    start with a vowel'''

    for word in wordlst:
        # if word begins with a vowel
        if word[0] in 'aeiouAEIOU':
            print( word )
            # dont return, it stops function, hence loop 
            # return word 
        
'''
>>> lst = ['apple','hello','pear','orange']
>>> vowelStart( lst )
apple
orange
>>>
'''











