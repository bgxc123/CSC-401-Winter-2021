# Strings1.py

##### str(ing) #####
'''

a str is a 0-based, indexed sequence of
characters, used for storing textual data

    DELIMIT a str with one of
    '',"",''''''

    \n is the newline character

    str

functions:
    len()
    max,min

operators:

    in, not in - work on substrings
    
    + - concatenation
    
    int*str, str*int - multiples
    
    <,>,<=,>=,==,!= - (dictionary order,
    but all upper case less than lower
    case)

indexing:
    
    s[i] - character at index i
    
    i = 0,...,len(s)-1, or
    
    i = -1,...,-len(s)

slicing:

    s[start:stop] - substring of s
    starting at index start (inclusive)
    and stopping at index stop (exclusive)

    start defaults to 0

    stop defaults to length

    s[start:stop:step]

    s[::-1] - reverse of s


>>> # create a str - delimit using quotes
>>> s = pear
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s = pear
NameError: name 'pear' is not defined
>>> s = 'pear'
>>> s
'pear'
>>> type(s)
<class 'str'>
>>> t = "apple"
>>> mine = "Eric's"
>>> mine
"Eric's"
>>> mine = 'Eric\'s'
>>> mine
"Eric's"
>>> 
>>> # computing the length
>>> len(t)
5
>>> sentence = "this is a string
SyntaxError: EOL while scanning string literal
>>> sentence = '' this is sentence
that runs
on multiple
lines. ''
>>> sentence
' this is sentence\nthat runs\non multiple\nlines. '
>>> # \n is a single character
>>> len( "\n\n\n")
3
>>> print( sentence )
 this is sentence
that runs
on multiple
lines. 
>>> 
>>> # operators for strings
>>> # in
>>> s
'pear'
>>> t
'apple'
>>> 'app' in 'apple'
True
>>> 'App' in 'apple' # case sensitive
False
>>> 'ale' in 'apple'
False
>>> 'Ap' not in 'apple'
True
>>> 
>>> # +, *
>>> s
'pear'
>>> s + 2
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s + 2
TypeError: can only concatenate str (not "int") to str
>>> s + '2' # concatenates
'pear2'
>>> s + ' ' + t
'pear apple'
>>> s*t
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s*t
TypeError: can't multiply sequence by non-int of type 'str'
>>> 3*s
'pearpearpear'
>>> t*5
'appleappleappleappleapple'
>>> 
>>> # dictionary comparisons, <,>,...
>>> 'apple' < 'pear'
True
>>> 'apple' < 'Pear'
False
>>> 'Z' < 'a'
True
>>> # ^^^ all upper case, less than all lower case
>>> 
>>> 
>>> # indexing
>>> s
'pear'
>>> s[1]
'e'
>>> s[0]
'p'
>>> s[3]
'r'
>>> # last character?
>>> t[3]
'l'
>>> t[len(t)-1] # last character
'e'
>>> s[len(s)-1] # last character
'r'
>>> # handy shorthand
>>> s[-1] # last character
'r'
>>> s[02]
SyntaxError: invalid token
>>> s[-2]
'a'
>>> s[-4]
'p'
>>> 
>>> # empty str
>>> s = " " # NOT the empty str
>>> len(s)
1
>>> s="" # empty str
>>> len(s)
0
>>> 
>>> # slicing
>>> s = 'apple'
>>> s[1]
'p'
>>> s[1:4] # slice
'ppl'
>>> s[0:2]
'ap'
>>> s[0:0]
''
>>> 
>>> # split railroad
>>> t = 'railroad'
>>> # rail
>>> t[0:4]
'rail'
>>> # road
>>> t[4:8]
'road'
>>> # start defaults to the beginning
>>> # stop defaults to the end
>>> t = 'railroad'
>>> t[:4]
'rail'
>>> t[4:]
'road'
>>> t[:]
'railroad'
>>> t[::2]
'rira'
>>> # niftiest trick of all
>>> t[::-1]
'daorliar'
>>>
'''
