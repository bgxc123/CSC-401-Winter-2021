# Lists.py

##### list #####

'''
list

    container that holds a sequence of
    items for any type. DELIMIT with []

    [item, item, item, ...]

    [] - empty list
    
    can mix types
    
    indexed, 0-based

    MUTABLE! (can be modified)

indexing

    lst[i]
    gets item at index i

    lst[i] = item
    sets item at index i

slicing

    lst[start:stop] 
    
    lst[start:stop:step]
    
functions

    len

    max, min

    sum
    
operators

    in, not in - works on entire ITEMS
    (not sublists, bit different from str)

    + - concatenates lists

    int*list, list*int

METHODS are functions with calling objects

    append(item) - adds item to end of
    list

    pop() - removes and RETURNS item at
    end of the list

    pop(index) - same but at index

    remove(item) - removes first occurence
    of item

    index(item) - returns location of
    item, error if not found

    sort() - sorts IN PLACE (MODFIES does
    NOT return).  (see also sorted() )

    reverse() - reverses in PLACE

    count(item) - returns count of item 

getting HELP

    we wont cover all the methods!

    Ctrl-SPACE or wait after . will show
    available methods

    dir(list) - displays methods

    help(list) - more detailed information

    help(list.pop) - info on particular
    method


>>> lst = [2,3,4.2,"apple",3<4]
>>> lst
[2, 3, 4.2, 'apple', True]
>>> type(lst)
<class 'list'>
>>> 
>>> # indexed, get items
>>> lst[0]
2
>>> lst[-1]
True
>>> 
>>> # indexed, set items
>>> lst
[2, 3, 4.2, 'apple', True]
>>> lst[1] = 99.9
>>> lst
[2, 99.9, 4.2, 'apple', True]
>>> # that doesnt work with str
>>> s = "apple"
>>> s[0] = 'A'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[0] = 'A'
TypeError: 'str' object does not support item assignment
>>> lst
[2, 99.9, 4.2, 'apple', True]
>>> lst[5] = 23
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lst[5] = 23
IndexError: list assignment index out of range
>>> 
>>> # also slices
>>> lst
[2, 99.9, 4.2, 'apple', True]
>>> lst[0:2]
[2, 99.9]
>>> lst[3:]
['apple', True]
>>> 
>>> # functions
>>> ls
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> lst
[2, 99.9, 4.2, 'apple', True]
>>> len(lst)
5
>>> max(lst)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    max(lst)
TypeError: '>' not supported between instances of 'str' and 'float'
>>> lst[3] = -12.4
>>> lst
[2, 99.9, 4.2, -12.4, True]
>>> max(lst)
99.9
>>> min(lst)
-12.4
>>> sum(lst)
94.7
>>> # average
>>> sum(lst)/len(lst)
18.94
>>> 
>>> 
>>> # containment - in, not in
>>> lst = [2,3,4.2,"apple",3<4]
>>> 'apple' in lst
True
>>> 'app' in lst
False
>>> 'app' in lst[3]
True
>>> [2,3] in lst
False
>>> [2] in lst
False
>>> 2 in lst
True
>>> 
>>> # note: check whether x is 2,3, or 4
>>> x = 7
>>> x==2 or x==3 or x==4
False
>>> # much slicker way to do same thing
>>> x in [2,3,4]
False
>>> 
>>> # +,*
>>> lst
[2, 3, 4.2, 'apple', True]
>>> lst + [2,3,4]
[2, 3, 4.2, 'apple', True, 2, 3, 4]
>>> lst
[2, 3, 4.2, 'apple', True]
>>> lst2 = lst + [2,3,4]
>>> lst2
[2, 3, 4.2, 'apple', True, 2, 3, 4]
>>> lst
[2, 3, 4.2, 'apple', True]
>>> lst + 2
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    lst + 2
TypeError: can only concatenate list (not "int") to list
>>> lst + [2]
[2, 3, 4.2, 'apple', True, 2]
>>> lst * 3
[2, 3, 4.2, 'apple', True, 2, 3, 4.2, 'apple', True, 2, 3, 4.2, 'apple', True]
>>> 
>>> # METHODS!
>>> lst
[2, 3, 4.2, 'apple', True]
>>> lst.append('pear') # lst is CALLING OBJECT
>>> lst
[2, 3, 4.2, 'apple', True, 'pear']
>>> lst.append( [2,3] )
>>> lst
[2, 3, 4.2, 'apple', True, 'pear', [2, 3]]
>>> lst[-1][1]
3
>>> lst[3][-1]
'e'
>>> lst
[2, 3, 4.2, 'apple', True, 'pear', [2, 3]]
>>> lst.pop()
[2, 3]
>>> lst
[2, 3, 4.2, 'apple', True, 'pear']
>>> item = lst.pop()
>>> lst
[2, 3, 4.2, 'apple', True]
>>> item
'pear'
>>> lst.pop(2)
4.2
>>> lst = [2,3,4,3,2,99]
>>> lst.remove( 4 )
>>> lst
[2, 3, 3, 2, 99]
>>> lst.remove(3)
>>> lst
[2, 3, 2, 99]
>>> lst.remove(5)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    lst.remove(5)
ValueError: list.remove(x): x not in list
>>> lst
[2, 3, 2, 99]
>>> lst.count(2)
2
>>> lst.count( 7 )
0
>>> # find first location of item
>>> lst.index( 3)
1
>>> lst.index(7)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    lst.index(7)
ValueError: 7 is not in list
>>> 
>>> lst
[2, 3, 2, 99]
>>> lst.append('apple')
>>> lst
[2, 3, 2, 99, 'apple']

>>> lst.sort()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    lst.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> lst.pop()
'apple'
>>> lst.pop()
99
>>> lst.sort()
>>> lst
[2, 2, 3]
>>> lst.reverse()
>>> lst
[3, 2, 2]
>>> lst = [2,7,6,2]
>>> lst[::-1]
[2, 6, 7, 2]
>>> lst
[2, 7, 6, 2]
>>> 
>>> 
>>> # getting help
>>> lst
[2, 7, 6, 2]
>>> type(lst)
<class 'list'>
>>> dir(lst)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(lst) # or help(list)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |
 
... some stuff omitted here ...


 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> help( lst.pop )
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> 

'''




