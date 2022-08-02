#Loops.py

# range
# iteration/for loop - REPEAT CODE

##### range #####
'''
a RANGE is an (arithmetic) sequence of
integers.

    BEHAVES like a list of numbers

    range(stop) "==" [0,1,...,stop-1]

    range(start,stop) "=="
    [start,start+1,...,stop-1]

    range(start,stop,step) "=="
    [start,start+step,..stop at stop...]

operations

    [] - indexing
    [:],[::] - slicing
    in - membership, iteration    
    can ITERATE/LOOP over a range!

>>> # range
>>> range(10)
range(0, 10)
>>> list( range(10) )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list( range(3,12) )
[3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list( range(3,27,2) )
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
>>> 4 in range(3,27,2)
False
>>> 5 in range(3,27,2)
True
>>> 27 in range(3,27,2)
False
>>> range(3,27,2)[0] # 0 steps
3
>>> range(3,27,2)[7] # 3+7*2
17
>>> 
>>> # a range doesnt actually store
>>> # the numbers
>>> range(1000000000000)
range(0, 1000000000000)
>>>
'''

##### for loop/iteration #####
'''
for <variable> in <sequence>:
    <indented statements>  # BODY

shorthand for a SEQUENCE of ASSIGNMENTS

EXECUTES the BODY (indented) for each
assignment

can ITERATE over:
- characters in a str
- items in a list
- numbers in a range

>>> # iteration using for loops
>>> s = 'abc'
>>> # print one character per line
>>> char = s[0]
>>> print( char )
a
>>> char = s[1]
>>> print( char )
b
>>> char = s[2]
>>> print( char )
c
>>> # ^ code REPETITIVE and depends
>>> # on knowledge of str s
>>> 
>>> # for loop BETTER, performs a
>>> # SEQUENCE of ASSIGNMENT statements
>>> s = 'abc'
>>> for char in s:
	print( char ) # body

	
a
b
c
>>> s = 'pear'
>>> for char in s:
	print( char ) # body

	
p
e
a
r
>>> 
>>> 
>>> 
>>> # can iterate over a list
>>> lst = [2,8,1,'apple']
>>> for item in lst:
	print( item )

	
2
8
1
apple
>>> 
>>> # CAUTION!
>>> s = "hello, how are you?"
>>> for word in s:
	print( word )

	
h
e
l
... edited out ...
o
u
?
>>> # ^ a str is a sequence of CHARACTERS
>>> # (not words), word is a TERRIBLE choice
>>> # for variable name here
>>> 
'''

##### for loop with an if #####
'''
>>> # print the numbers in range(3,100,4)
>>> # that are divisble by 5
>>> 
>>> # first, print all the numbers
>>> for num in range(3,100,4):
	print(num)

	
3
7
11
15
19
23
27
31
35
... edited out ...
95
99
>>> for num in range(3,100,4):
	if num%5==0:# divisible by 5
		print(num)

		
15
35
55
75
95
>>>
'''
