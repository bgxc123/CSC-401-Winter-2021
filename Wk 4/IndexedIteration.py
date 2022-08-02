# IndexedIteration.py

##### counter/index/range iteration #####
'''
Idea: ITERATE over the INDICES of an
object rather than the object itself.

for i in range(len(s)):
    print( i, s[i] )

The INDICES of object are given by:
range(len(object)).  For example:

range(len('apple')) "==" [0,1,2,3,4]

TIP: if you can, use NON-indexed
iteration. However, sometimes you MUST use
indexed iteration, in particular when you
NEED INDEX/LOCATION information.

TIP: also see enumerate()
'''

##### standard vs indexed iteration #####
'''
>>> # standard iteration
>>> # uses iterator
>>> s = 'pear'
>>> for c in s:
	print( c )

	
p
e
a
r
>>> 
>>> # indexed iteration
>>> s = 'pear'
>>> for i in range(len(s)):
	print( i, s[i] )

	
0 p
1 e
2 a
3 r
>>> 
>>> # note that range(len(object))
>>> # is set of indices
>>> s
'pear'
>>> len(s)
4
>>> range(len(s))
range(0, 4)
>>> list( range(len(s)) )
[0, 1, 2, 3]
>>>
'''

##### indexed accumulator #####
'''
make this work:
>>> vowelIndices( 'hello, how are you?' )
[1, 4, 8, ...]
'''

def vowelIndices( phrase ):
    indices = []
    for i in range(len(phrase)):
        if phrase[i] in 'aeiou':# a vowel
            #print(i, phrase[i] )
            indices.append( i )
    return indices
                       
##### indexed search #####
'''
make this work: return first index
of a vowel, or -1 if none exists

>>> firstVowel('hello, how are you?')
1 # index of "e" first vowel
>>> firstVowel('jdjsdjfj')
-1 # no vowel found
'''

def firstVowel( phrase ):
    for i in range(len(phrase)):
        if phrase[i] in 'aeiou':# a vowel
            #print(i, phrase[i] )
            return i
    return -1
            
            













