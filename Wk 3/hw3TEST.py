# hw3TEST.py

>>> from hw3 import *

##### cheer #####

>>> cheer('Huskies')
How do you spell winner?
I know, I know!
H U S K I E S !
And that's how you spell winner!
Go Huskies!
>>> cheer('Bears')
How do you spell winner?
I know, I know!
B E A R S !
And that's how you spell winner!
Go Bears!
>>> cheer('Koalas')
How do you spell winner?
I know, I know!
K O A L A S !
And that's how you spell winner!
Go Koalas!
>>> 

##### vowelCount ######

>>> vowelCount('Le Tour de France')
a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times.
>>> vowelCount('The quick red fox jumped over the lazy brown dog.')
a, e, i, o, and u appear, respectively, 1, 5, 1, 4, 2 times.
>>> vowelCount('zmrzlna')
a, e, i, o, and u appear, respectively, 1, 0, 0, 0, 0 times.
>>> 

##### crypto ######

>>> crypto('crypto.txt')
I will tell you my xxxxxx. But first, I have to explain
why it is a xxxxxx.
<BLANKLINE>
And that is all I will tell you about my xxxxxx.
<BLANKLINE>
>>> 

##### links ######

>>> links('twolinks.html')
2
>>> links('twolinks.html')==2
True
>>> links('crypto.txt')
0
>>> links('crypto.txt')==0
True
>>> 

##### duplicate ######

>>> duplicate('Duplicates.txt')
True
>>> duplicate('Duplicates.txt')==True
True
>>> duplicate('noDuplicates.txt')
False
>>> duplicate('noDuplicates.txt')==False
True
>>> 
