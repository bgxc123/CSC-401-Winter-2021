# WhileLoops.py

##### while loop #####
'''
while <condition>:
    <body>
<rest of your code>

while
- "repeating if" statement
- EXECUTE the BODY as long as the as the
  condition is True. STOP when False, and
  proceed to rest of code.
- more general purpose, trickier to write

TIP: when possible USE a FOR loop. but
sometimes have to use a WHILE loop, in
particular when you DON'T KNOW ahead of
time WHAT you are going to ITERATE over.

body of the loop may execute
0,1,2,... infinite number of times

important: condition should become False
(or have some other way of stopping loop)

for/while loop MODIFIERS:

return - terminates function, hence loop
break - terminates innermost loop
continue - termininates current iteration,
           skips to next iteration
pass - does nothing
'''

##### while example #####

'''
want this to work:

>>> pigLatin('apple')
'appleay'
>>> pigLatin('pear')
'earpay'
>>> pigLatin('string')
'ingstray'
'''

# v1 - WRONG - only moves ONE consonant

def pigLatin( word ):

    # if word begins consonant, move to back
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    return word + 'ay'

'''
>>> pigLatin('apple')
'appleay'
>>> pigLatin('pear')
'earpay'
>>> pigLatin('string')
'tringsay'
>>>
'''

# v2 - better but still BAD
# handles 3 (or n) consonants with n
# if statements. BUT, what is n? And,
# does EXTRA work for words with
# fewer consonants.

def pigLatin( word ):

    # if word begins consonant, move to back
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    if word[0] not in 'aeiou':
        word = word[1:] + word[0]
    return word + 'ay'



# v1 - CORRECT - does EXACTLY the right
# amount of work

def pigLatin( word ):

    # moves consonant CLUSTER to back
    while word[0] not in 'aeiou':
        word = word[1:] + word[0]
    return word + 'ay'

'''
>>> pigLatin('string')
'ingstray'
>>> pigLatin('apple')
'appleay'
>>> pigLatin('pear')
'earpay'
>>> pigLatin('zmrzlina') # Czech
'inazmrzlay'
>>>

following causes an INFINITE loop (no
vowel).  CTRL-C to terminate.

>>> pigLatin('why')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pigLatin('why')
  File "C:\Users\esedgwic\Dropbox\courses\csc401\lectures\WhileLoops.py", line 93, in pigLatin
    while word[0] not in 'aeiou':
KeyboardInterrupt
>>>
'''










