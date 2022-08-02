# Conditionals.py

# code that may or may not execute
# three (standard) flavors:

# if - OPTION (executes or not)
# if/else - EXACTLY 1 of 2
# if/elif/.../else - EXACTLY 1 of n

##### if #####

'''
if <condition>:
    <indented statements> # body
<non-indented statements>

one way if statement
- an OPTION
- indented block of code either
  executes or not
- if condition (boolean expression)is True,
  execute body, otherwise do nothing
- in either case, continue with
  non-indented statements
'''

'''
want this to work:
>>> votingAge(20.3)
You are old enough to vote.
Bye.
'''

def votingAge(age):
    '''determines whether person with
    given age is old enough to vote'''

    if age>=18: # old enough to vote
        print('You are old enough to vote.')
    print('Bye.')

'''
>>> votingAge(23.2)
You are old enough to vote.
Bye.
>>> votingAge(16.5)
Bye.
>>>
'''
    

##### if/else #####

'''
if <condition>:
    <indented statements> # body
else:
    <indented statements> # body
<non-indented statements>

CHOICE of EXACTLY 1 of 2 blocks of code

Evaluate the CONDITION. If it is True,
execute the if block.  Otherwise, execute
the else block.  In either case, continue
with non-indented statements.

want this to work:

>>> votingAge(22.3)
You are old enough to vote.
Bye.
>>> votingAge(16)
You can't vote.
Wait 2 years.
Bye.
'''

#v2 - runs correctly
#but BAD style
def votingAge(age):
    '''determines whether person with
    given age is old enough to vote, if
    not tells them how long to wait'''

    if age>=18: # old enough to vote
        print('You are old enough to vote.')
    if age<18: # NOT old enough to vote
        print('You can\'t vote.')
        print('Wait', 18-age ,'years')
    print('Bye.')

'''
>>> votingAge(23.2)
You are old enough to vote.
Bye.
>>> votingAge(16.5)
You can't vote.
Wait 1.5 years
Bye.
>>>
'''

#v3 - GOOD version
def votingAge(age):
    '''determines whether person with
    given age is old enough to vote, if
    not tells them how long to wait'''

    if age>=18: # old enough to vote
        print('You are old enough to vote.')
    else: # NOT old enough to vote
        print('You can\'t vote.')
        print('Wait', 18-age ,'years')
    print('Bye.')

'''
>>> votingAge(23.2)
You are old enough to vote.
Bye.
>>> votingAge(16.5)
You can't vote.
Wait 1.5 years
Bye.
>>>
'''
##### if/elif/else ######

'''
if <condition>:
    <block>
elif <condition>:
    <block>
elif <condition>:
    <block>
...
else:
    <block>

EXACTLY ONE of the indented blocks will
execute, the first whose condition is True
or the else if none are True.

make this work: (DISCRETIZE a range of
values)

>>> status(67.3) # temperature fahrenheit
'warm'
>>> status(30)
'cool'
>>> status(-13.2)
'cold'
>>> status(99)
'hot'
'''


# DONT do this
# not as efficient
# EASIER to make MISTAKE
# HARDER to MAINTAIN
def status(temp):
    '''return status, hot/warm/cool/cold,
    of given temperature'''
    if temp>=80:
        return 'hot'
    elif temp<80 and temp>=50:
        return 'warm'
    elif temp<50 and temp>=10:
        return 'cool'
    else:
        return 'cold'


# one sided conditions are
# SIMPLER, FASTER, and EASIER to MAINTAIN
def status(temp):
    '''return status, hot/warm/cool/cold,
    of given temperature'''
    if temp>=80:
        return 'hot'
    elif temp>=50:
        return 'warm'
    elif temp>=10:
        return 'cool'
    else:
        return 'cold'

'''
>>> status(67.3)
'warm'
>>> status(30)
'cool'
>>> status(-13.2)
'cold'
>>> status(99)
'hot'
>>>
'''











