# NestedLoops.py

##### 2d/nested iteration #####
'''
2D or NESTED iteration is a loop INSIDE
another loop, e.g:

for  # outer loop
    for # inner loop

The inner loop will RUN to COMPLETION
within each iteration of the outer loop.

TIP (OBVIOUS): Code IN loop will be
REPEATED.
'''

##### a NESTED list  #####

lst = [
['apple','pear','kiwi'],
['pizza','msg','salt'],
['cereal','chips','velveeta','cookies']]

'''
>>> lst
[['apple', 'pear', 'kiwi'], ['pizza', 'msg', 'salt'], ['cereal', 'chips', 'velveeta', 'cookies']]
>>> lst[2]
['cereal', 'chips', 'velveeta', 'cookies']
>>> lst[2][3]
'cookies'
>>> lst[2][3][-1]
's'
>>> for row in lst:
	print( row )

	
['apple', 'pear', 'kiwi']
['pizza', 'msg', 'salt']
['cereal', 'chips', 'velveeta', 'cookies']
>>> for row in lst:
	for item in row:
		print( item )

		
apple
pear
kiwi
pizza
msg
salt
cereal
chips
velveeta
cookies
>>> for row in lst:
	for item in row:
		print( item, end=' ')

		
apple pear kiwi pizza msg salt cereal chips velveeta cookies 
>>> for row in lst:
	for item in row:
		print( item, end=' ')
	print()

	
apple pear kiwi 
pizza msg salt 
cereal chips velveeta cookies 
>>>
'''

##### 2d search #####

lst = [
['apple','pear','kiwi'],
['pizza','msg','salt'],
['cereal','chips','velveeta','cookies']]

'''
make this work:
>>> contains( 'kiwi', lst )
True
>>> contains( 'Kiwi', lst )
False
'''

# 2d (nested) search
def contains( target, lst2d ):

    for row in lst2d:
        for item in row:
            if item == target:
                #print( item )
                return True
    return False


##### 2d, indexed, accumulator #####

# Treasure Map!

# \ continues statement on next line
treasureMap =\
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~X~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~============~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~====X==============~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~======================~~~~~~~~~~~~~~~~~~
~~~~~~~~=========================~~~~~~~~~~~~~~~~~~~
~~~~~~~~~==========X=========X=======~~~~~~~~~~~~~~~
~~~~~~~~~=========================~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~===================~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~=======================~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~========================~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~=======X==========X==~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~====================~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~==================~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~=================~~~~~~~~~~~~~~~~~~~~~~~
~~~~X~~~~~~~~~============~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
'''
make this work:
>>> getTreasure( treasureMap )
[(1,4),(3,?),...]
'''

def getTreasure( tmap ):
    ''' return list of (row,col) locations
    of all treasure (X) on tmap'''
    treasure = []
    tmap = tmap.split() # break into lines
    for row in range(len(tmap)):
        # print( row, tmap[row] )
        for col in range(len(tmap[row])):
            if tmap[row][col]=='X':
                #print(row,col,tmap[row][col])
                treasure.append((row,col))
    return treasure

'''
>>> getTreasure( treasureMap )
[(1, 4), (3, 16), (6, 19), (6, 29), (11, 20), (11, 31), (15, 4)]
>>>
'''








