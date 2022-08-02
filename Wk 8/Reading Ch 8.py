#Ch 8 Reading#

#deck of cards class#
import random
class Deck:
    
    suits = {'\u2660','\u2661','\u2662','\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self):
        self.deck = []
        for i in Deck.suits:
            for j in Deck.ranks:
                self.deck.append(j+i)

    def __repr__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

#PP 8.5#
class Deckv2:
    
    def __init__(self,cards):
        self.deck = []
        for i in cards:
            self.deck.append(i)

##    def __repr__(self):
##        return str(self.deck)
##    def __eq__(self,other):
##        return self.deck == self.other

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

#queue class
class Queue:
    def __init__(self,queue=None):
        if queue == None:
            self.queue = []
        else:
            self.queue = queue
    def __repr__(self):
        return 'Queue({})'.format(self.queue)

    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return (len(self.queue) == 0)


#PP 8.7#
class Deckv3:
    
    suits = {'\u2660','\u2661','\u2662','\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self,deck=None):
        if deck == None:
            for i in Deck.suits:
                for j in Deck.ranks:
                    self.deck.append(j+i)
        else:
            self.deck = deck
        

    def __repr__(self):
        return 'Deck({})'.format(self.deck)

    def __eq__(self,other):
        return self.deck == other.deck

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

###PP 8.8 #
##class Vector(Point):
##    def __repr__(self):
##        return 'Vector {}'.format(self.get())
##    
##    def __add__(self,v):
##        return Vector(self.x+v.x, self.y+v.y)
##    def __mul__(self,v):
##        return self.x*v.x+ self.y*v.y

        
#PP 8.9#
class Queue2:
    def __init__(self,queue=None):
        if queue == None:
            self.queue = []
        else:
            self.queue = queue
    def __repr__(self):
        return 'Queue({})'.format(self.queue)

    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.queue == []:
            raise KeyboardInterrupt('dequeue from empty queue')
        else:
            return self.queue.pop(0)
    def isEmpty(self):
        return (len(self.queue) == 0)
        
        
        
