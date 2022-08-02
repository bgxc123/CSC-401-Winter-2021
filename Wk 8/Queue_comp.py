# Queue_comp.py

# Queue class
    # CONTAINER class
    # IMPLEMENTATION 1 of 2
    # COMPOSITION!  (2nd - inheritance)

##### "review" - assignment/copies #####
'''
ASSIGNMENT(=) - makes two names refer to
the SAME object.  All modifications using
one name are seen using the other name
(because they are the same object)

>>> lst = [2,3,4]
>>> lst2 = lst
>>> lst.append(5)
>>> lst
[2, 3, 4, 5]
>>> lst2
[2, 3, 4, 5]
>>> lst2.append(6)
>>> lst2
[2, 3, 4, 5, 6]
>>> lst
[2, 3, 4, 5, 6]
>>> lst.pop()
6
>>> lst
[2, 3, 4, 5]
>>> lst2
[2, 3, 4, 5]
>>> lst == lst2
True
>>> lst is lst2 # same object in memory
True

wont be a problem for immutable objects

>>> x = 5
>>> y = x
>>> x is y
True

If you want a COPY, call the CONSTRUCTOR.

>>> lst = [2,3,4]
>>> lst2 = list(lst) # make a NEW one (copy)
>>> lst.append(5)
>>> lst
[2, 3, 4, 5]
>>> lst2
[2, 3, 4]
>>> lst is lst2
False
'''

##### Queue - COMPOSITION #####

# see queuesTEST.py

# IMPLEMENTATION: COMPOSITION
    # list is an ATTRIBUTE of self
    # mantra: list is called self.q

# which methods?
    # MODIFY/SET
    # RETURN/GET
    # BOTH

class Queue:

    # header only runs once
    def __init__(self,lst=[]): # runs once
        # body runs every time!
        # fix: call constructor in body
        self.q = list(lst)

    def __repr__(self):
        return f"Queue({self.q})"
        return "Queue({})".format(self.q)

    def enqueue(self,item): # set/modify
        self.q.append(item)

    def dequeue(self): # modifies and returns
        item = self.q.pop(0)
        return item
        # or
        return self.q.pop(0)

    # q[1] -> Queue.__getitem__(q,1)
    # get some things for FREE:
    # iteration - for/in
    # containment - in
    def __getitem__(self,index):
        return self.q[index]

    # len(q) -> Queue.__len__(q)
    def __len__(self): # get
        return len(self.q)

    # q1 == q2 -> Queue.__eq__(q1,q2)
    def __eq__(self,other):
        return self.q==other.q # compare lists
        # or
        if self.q==other.q:
            return True
        else:
            return False

    def __add__(self,other):
        # return a NEW Queue
        # NOT a list
        return Queue(self.q + other.q)

'''

before fixing __init__ we had the
following problem.  2 queues were sharing
the same contents:

>>> q1 = Queue()
>>> q2 = Queue()
>>> q1.enqueue()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    q1.enqueue()
TypeError: enqueue() missing 1 required positional argument: 'item'
>>> q1.enqueue(2)
>>> q2.enqueue('apple')
>>> q1
Queue([2, 'apple'])
>>> q2
Queue([2, 'apple'])
>>> q1 == q2
True
>>> q1 is q2
False
>>> # but underlying lists are the same
>>> q1.q is q2.q
True
>>>
'''

##### doctest #####
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile('queuesTEST.py'))
    
    
    
























