# Dictionaries.py

##### dict(ionary) #####
'''
dict
- {key:val, key:val, ...}
- {} empty dictionary
- container for key:val pairs
  like a list, but indexed by keys
- insertion ordered
- dictionaries are MUTABLE
- keys must be UNIQUE/IMMUTABLE/hashable
- dictionaries are FAST

operators

- d[key] - return key's value (getitem)
- d[key]=value, sets key:value (setitem)
- in, not in - work on keys not values
  for containment and iteration

methods
- pop(key) - deletes pair, returns value
(.values(), .items(), .keys(), .update() )

suppose that we want to write a phonebook
application.  Given a name, we want to
retrieve the corresponding phone number.

how do we store the data?

names = ['frank','sue','sally']
numbers = [111,222,333]

or

phonenums = \
[('frank',111),('sue',222),('sally',333)]

>>> # dict is much better
>>> phonenums = {'frank':111, 'sue':222, 'sally':333}
>>> phonenums
{'frank': 111, 'sue': 222, 'sally': 333}
>>> phonenums['sue'] # 'sue' is key
222
>>> phonenums['sally'] # 'sue' is key
333
>>> # can also assign
>>> phonenums['fred'] = 555
>>> phonenums
{'frank': 111, 'sue': 222, 'sally': 333, 'fred': 555}
>>> phonenums['frank'] = 777
>>> phonenums
{'frank': 777, 'sue': 222, 'sally': 333, 'fred': 555}
>>> # can I change a key?
>>> # sue -> Sue?
>>> # no, but can remove and reenter
>>> phonenums.pop('sue')
222
>>> phonenums
{'frank': 777, 'sally': 333, 'fred': 555}
>>> phonenums['Sue'] = 222
>>> phonenums
{'frank': 777, 'sally': 333, 'fred': 555, 'Sue': 222}
>>> # ==  - order doesnt matter
>>> {'a':1, 'b':2} == {'b':2, 'a':1}
True
>>> # in - works on keys not values
>>> phonenums
{'frank': 777, 'sally': 333, 'fred': 555, 'Sue': 222}
>>> 333 in phonenums
False
>>> 'sally' in phonenums
True
>>> for key in phonenums:
	print( key, phonenums[key])

	
frank 777
sally 333
fred 555
Sue 222
>>> for key in sorted(phonenums):
	print( key, phonenums[key])

	
Sue 222
frank 777
fred 555
sally 333
>>> phonenums
{'frank': 777, 'sally': 333, 'fred': 555, 'Sue': 222}
>>> phonenums[ ['Curie','Marie']] = 888
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    phonenums[ ['Curie','Marie']] = 888
TypeError: unhashable type: 'list'
>>> phonenums[('Curie','Marie')] = 888
>>> phonenums
{'frank': 777, 'sally': 333, 'fred': 555, 'Sue': 222, ('Curie', 'Marie'): 888}
>>> 
'''

##### dict example - frequency counting #####


'''
make this work, count the frequency of
every item in a list

>>> frequencies( [5,8,5,8,7] )
{5:2, 8:2, 7:1}
'''

# accumulate a dict!
def frequencies( iterable ):
    ''' return a dictionary with frequency
    counts of the items in a lst'''

    counts = {}
    for item in iterable:

        # if item is new, add key
        # with a count of 1
        if item not in counts:
            counts[item]=1
        # otherwise, increase count
        # by 1
        else:
            counts[item]+=1
    return counts
    
'''
>>> frequencies( [5,8,5,8,7] )
{5: 2, 8: 2, 7: 1}
>>> frequencies( 'abracadabra' )
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
>>>
'''














