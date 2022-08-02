# DebuggingTracing.py



##### Debugging #####
'''
A BUG is an ERROR in your code that causes
it to CRASH or produce an INCORRECT
result. Types:
- SYNTAX (=/==)
- LOGIC

Writing code:
- BABY STEPS - write code bit by bit
- TEST constantly
- FIX BUGS - don't write more code
- BACK UP - comment out code

To DEBUG:
- WHERE is the bug?
- WHAT is the bug?

Tools: 
- TRACE code
- RUBBER DUCK debugging
- PRINT variables 
- print( vars() )
- DEBUGGER (Shell>Debug>Debugger )
'''

##### Tracing code #####
'''
TRACE code - run code "by hand" keeping
track of all variables.
'''
##### h #####

def h(s):
    n=0
    m=0
    print( vars() )
    for c in s:
        if c not in 'aeiou':
            n+=1
            m = max(m,n)
        else:
            n=0
        print( vars() )
    return m

'''
h computes the maximum number of consecutive
consonants in the given string s

n = current number of consecutive consonants
m = maximum value of all the n's that have
    been seen

>>> h('fighter')
3
>>> h('mississippi')
??

using print( vars() )

>>> h('fighter')
{'s': 'fighter', 'n': 0, 'm': 0}
{'s': 'fighter', 'n': 1, 'm': 1, 'c': 'f'}
{'s': 'fighter', 'n': 0, 'm': 1, 'c': 'i'}
{'s': 'fighter', 'n': 1, 'm': 1, 'c': 'g'}
{'s': 'fighter', 'n': 2, 'm': 2, 'c': 'h'}
{'s': 'fighter', 'n': 3, 'm': 3, 'c': 't'}
{'s': 'fighter', 'n': 0, 'm': 3, 'c': 'e'}
{'s': 'fighter', 'n': 1, 'm': 3, 'c': 'r'}
3
>>> 
'''

##### d #####

def d(n):
    n = abs(n)
    c = 0
    print( vars() )
    while n>0:
        n//=10  # n = n//10
        c+=1
        print( vars() )
    return c

'''
>>> d(165)
3
>>> d(123456789)
?

>>> d(165)
{'n': 165, 'c': 0}
{'n': 16, 'c': 1}
{'n': 1, 'c': 2}
{'n': 0, 'c': 3}
3
>>>

computes the number of digits (base 10)
'''

##### practice on your own! #####

##### f #####

def f(s):
    x=0
    for i in range(len(s)):
        if s[i] == s[i].upper():
            x+=i
    return x

'''
>>> f('abcABC')
??
>>> f('HowAREYou')
??
'''

##### g #####

def g(nums):
    answer = []
    for num in nums:
        if num%2==0:
            answer.append( num )
    return answer

'''
>>> g( range(0,100,5) )
???
>>> g( range(0,100,7) )
???
'''


















