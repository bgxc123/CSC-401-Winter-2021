# Randomness.py

##### random module #####
'''
random module contains functions that
generate (psuedo) random numbers/choices.

import random

functions:

- randrange(n) - random int from range(n)
- randrange(start,stop) - returns random
  int from range(start,stop)
- choice(sequence) - returns random item
  from sequence
- seed(n) - seeds random number generator
  so results can be replicated

also:
- uniform - generate random float
- shuffle
- sample(sequence,n) - return n items
  chosen randomly from sequence

>>> import random
>>> random
<module 'random' from 'C:\\Users\\esedgwic\\AppData\\Local\\Programs\\Python\\Python37\\lib\\random.py'>
>>> 
>>> # random integers
>>> random.randrange(3) # 0,1,2
1
>>> random.randrange(3) # 0,1,2
2
>>> random.randrange(3) # 0,1,2
1
>>> random.randrange(3) # 0,1,2
0
>>> random.randrange(3) # 0,1,2
1
>>> [random.randrange(3) for i in range(20)]
[1, 0, 1, 2, 1, 0, 2, 0, 1, 0, 1, 1, 1, 2, 0, 2, 1, 2, 1, 0]
>>> [random.randrange(1,7) for i in range(20)]
[3, 2, 5, 3, 6, 5, 4, 6, 6, 6, 1, 4, 5, 4, 4, 2, 1, 5, 4, 3]
>>> # random floats
>>> [random.uniform(0,1) for i in range(20)]
[0.8230817351880068, 0.7038126689606211, 0.9925452252005018, 0.3954698107350011, 0.24772428020760162, 0.5776371291606074, 0.16205674208838416, 0.9696665136827045, 0.6955233193035627, 0.43627448531181556, 0.804406990689755, 0.028841069718927637, 0.1321257119963054, 0.41229932207995046, 0.8550574349378842, 0.6284301490577197, 0.5449881865634275, 0.3849576503785922, 0.33726641136567537, 0.9150576626753376]
>>> 
>>> # random choices
>>> random.choice( [1,'apple',3])
3
>>> random.choice( [1,'apple',3])
3
>>> random.choice( [1,'apple',3])
'apple'
>>> random.choice( [1,'apple',3])
1
>>> # coin flips
>>> [ random.choice("HT") for i in range(20)]
['H', 'T', 'T', 'H', 'H', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'H']
>>> random.sample( range(10), 3)
[0, 5, 6]
>>> random.sample( range(10), 3)
[6, 4, 9]
>>> 
>>> lst = list(range(10))
>>> lst
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> # shuffle
>>> random.shuffle( lst )
>>> lst
[6, 0, 9, 3, 2, 1, 8, 7, 5, 4]
>>> random.shuffle( 'abc' )
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    random.shuffle( 'abc' )
  File "C:\Users\esedgwic\AppData\Local\Programs\Python\Python37\lib\random.py", line 278, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment
>>> [ random.choice("HT") for i in range(20)]
['T', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'H', 'T']
>>> [ random.choice("HT") for i in range(20)]
['T', 'H', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H']
>>> # seeding allows you to repeat
>>> # random sequence
>>> random.seed(0)
>>> [ random.choice("HT") for i in range(20)]
['T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T']
>>> random.seed(0)
>>> [ random.choice("HT") for i in range(20)]
['T', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T']
>>> random.seed(76)
>>> [ random.choice("HT") for i in range(20)]
['T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H']
>>> random.seed(76)
>>> [ random.choice("HT") for i in range(20)]
['T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H']
>>> 
'''

