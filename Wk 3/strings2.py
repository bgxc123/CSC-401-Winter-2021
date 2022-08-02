#Strings2.py

##### terminology: FUNCTIONS vs. METHODS #####
'''
FUNCTIONS are called directly

print(4.3)
abs(-44)
max(lst)

METHODS have CALLING OBJECTS, and a "." to
the left

lst = []
lst.append( 4 )
lst.pop()
'''

##### str METHODS #####
'''
reminder: help(str) or dir(str),
help(str.find)

str(ings) are IMMUTABLE 
- cant change them
- but you can produce new ones
  based on old ones
- and you can reassign

index/slice

functions - len

METHODS:

    upper/lower

    split(sep=' ') - splits a str into  a LIST of strs, sep
    character defaults to whitespace

    find(target) - return index, -1 if not
    found

    index(target) - returns index, error
    if not found

    replace(old,new)

    count(target) - counts occurences of
    substring target

    format() - fill in {} placeholders
    with variables/values

    f-string - similar to format (but more
    concise), NOT in book

'''

>>> # lists are MUTABLE, can be changed
>>> lst = [2,3,4]
>>> lst[1] = 99
>>> lst
[2, 99, 4]
>>> # str's are IMMUTABLE, cannot be changed
>>> s = "apple"
>>> s[0] = "A"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[0] = "A"
TypeError: 'str' object does not support item assignment
>>> 
>>> # upper/lower
>>> s
'apple'
>>> s.upper()
'APPLE'
>>> s
'apple'
>>> # capitalize s
>>> s[0].upper() + s[1:]
'Apple'
>>> s = s[0].upper() + s[1:]
>>> s
'Apple'
>>> 
>>> s = 'apple'
>>> s.capitalize()
'Apple'
>>> 'Fred'.lower()
'fred'
>>> 
>>> # good use of upper/lower
>>> # case INSENSITIVE comparison
>>> s = 'Apple'
>>> s2 = 'aPpLe'
>>> s == s2
False
>>> s.upper() == s2.upper()
True
>>> 
>>> # split
>>> sentence = 'Hello, how are you?'
>>> for word in sentence:
	print( word )

	
H
e
l
... some lines deleted ...
o
u
?
>>> 
>>> 
>>> sentence
'Hello, how are you?'
>>> sentence.split()
['Hello,', 'how', 'are', 'you?']
>>> wordlst = sentence.split()
>>> for word in wordlst:
	print( word )

	
Hello,
how
are
you?
>>> 
>>> "3,4,5,11,5".split()
['3,4,5,11,5']
>>> "3,4,5,11,5".split(",")
['3', '4', '5', '11', '5']
>>> 
>>> # find/index
>>> sentence
'Hello, how are you?'
>>> sentence.find('how')
7
>>> sentence.find('How')
-1
>>> # index is similar
>>> sentence.index('how')
7
>>> sentence.index('How')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sentence.index('How')
ValueError: substring not found
>>> 
>>> # count
>>> sentence.count('h')
1
>>> sentence
'Hello, how are you?'
>>> # count upper and lower case
>>> sentence.lower().count('h')
2
>>> 
>>> # replace
>>> s = 'Hello, how are you?'
>>> s.replace(',','')
'Hello how are you?'
>>> s.replace('?','')
'Hello, how are you'
>>> s = 'Hello, how are you?'
>>> s.replace(',','').replace('?','')
'Hello how are you'
>>> s.replace(',','').replace('?','').upper()
'HELLO HOW ARE YOU'
>>> s.replace(',','').replace('?','').upper().split()
['HELLO', 'HOW', 'ARE', 'YOU']
>>> s.split().replace(',','').replace('?','').upper()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.split().replace(',','').replace('?','').upper()
AttributeError: 'list' object has no attribute 'replace'
>>> s
'Hello, how are you?'
>>> # print one word per line, all upper
>>> # case and no punctuation
>>> for word in s.replace(',','').replace('?','').upper().split():
	print( word )

	
HELLO
HOW
ARE
YOU
>>> 
>>> # format method and f-strings
>>> person = "Napoleon"
>>> item = "ducks"
>>> amount = 100
>>> letter = '''Dear {},
How are you? Would you like to buy
some {} for ${}'''
>>> letter
'Dear {},\nHow are you? Would you like to buy\nsome {} for ${}'
>>> letter.format(person,item,amount)
'Dear Napoleon,\nHow are you? Would you like to buy\nsome ducks for $100'
>>> 
>>> # f-strings, NOT in the book
>>> # but very succint
>>> f'''Dear {person},
How are you? Would you like to buy
some {item} for ${amount}'''
'Dear Napoleon,\nHow are you? Would you like to buy\nsome ducks for $100'
>>> 

