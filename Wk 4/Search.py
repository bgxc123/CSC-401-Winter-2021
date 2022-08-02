# Search.py

##### search pattern #####

# not explicitly mentioned in book

'''
A (linear) SEARCH iterates over data to
determine whether a given condition holds.
IF SO, the code STOPS.  But to conclude
the condtion does NOT hold, the code must
examine ALL data.  A search typically
looks like this:

for
    if
        return
return

TIP: be careful about return IN a loop
'''

##### search example #####

'''
make this work:
>>> hasVowel("hello how are you?")
True
>>> hasVowel("sdjflkjsdkljflsfdj")
False
'''

# v1 - BAD - OBVIOUSLY wrong
# only one performs one iteration
# i.e, only examines first character

def hasVowel( s ):
    for char in s:
        if char in 'aeiou': # found vowel
            #print(char)
            return True
        else:
            return False
'''
>>> hasVowel("apple")
True
>>> hasVowel("djljdsfsjd")
False
>>> hasVowel('pear')
False
>>>
'''

        
# v2 - GOOD version
# second return AFTER the loop
def hasVowel( s ):
    for char in s:
        if char in 'aeiou': # found vowel
            #print(char)
            return True
    return False

'''
>>> hasVowel("apple")
True
>>> hasVowel("djljdsfsjd")
False
>>> hasVowel('pear')
True
>>>
'''





























