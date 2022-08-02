# ListComprehensions.py

##### list comprehension #####

'''
[expression for item in iterable if
condition]

list comprehensions:
- one line ACCUMULATOR
- not in the textbook
- very useful
- SAME for: dict, set, tuple

>>> # [0,1,4,9,...,100]
>>> # accumulator
>>> squares = []
>>> for i in range(11):
	squares.append( i*i )

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> # same thing with a list comprehension
>>> [i*i for i in range(11)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> squares = [i*i for i in range(11)]
>>> [i*i for i in range(11) if i%3!=0]
[1, 4, 16, 25, 49, 64, 100]
>>> 
>>> # build combinations with
>>> # nested comprehension
>>> games = [ ('R','R'), ('R','S'), ...]
>>> [(p1,p2) for p1 in 'RPS' for p2 in 'RPS']
[('R', 'R'), ('R', 'P'), ('R', 'S'), ('P', 'R'), ('P', 'P'), ('P', 'S'), ('S', 'R'), ('S', 'P'), ('S', 'S')]
>>> 
>>> 
>>> # can also do this for set, dict, tuple
>>> # tuple - generator
>>> [i*i for i in range(11)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> (i*i for i in range(11))
<generator object <genexpr> at 0x0000023E218ADF48>
>>> for n in (i*i for i in range(11)):
	print( n )

	
0
1
4
9
16
25
36
49
64
81
100
>>> (i*i for i in range(11))[3]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    (i*i for i in range(11))[3]
TypeError: 'generator' object is not subscriptable
>>> 
'''
