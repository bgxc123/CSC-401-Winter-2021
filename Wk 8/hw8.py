#hw8.py#
#Name: Brendan Gee
#Contributors:
#Sources:

#Pizza#
class Pizza:
    def __init__(self,size='M',toppings=set()): #default size & empty set (not dict)
        self.size = size
        self.toppings = set(toppings) #creates a distinct set each time pizza obj is initialized

    def __repr__(self): #return
        return f"Pizza('{self.size}',{self.toppings})"

    def __eq__(self,other): #return
        return self.size == other.size and self.toppings == other.toppings

    def setSize(self,s): #modify
        self.size = s 

    def getSize(self): #return
        return self.size

    def addTopping(self,item): #modify
        self.toppings.add(item)

    def removeTopping(self,item): #modify
        self.toppings.remove(item)

    def price(self): #return
        if self.size == 'S':
            return 6.25 + .70*len(self.toppings)
        elif self.size == 'M':
            return 9.95 + 1.45*len(self.toppings)
        elif self.size == 'L':
            return 12.95 + 1.85*len(self.toppings)

        
#orderPizza
def orderPizza():
    print('Welcome to Python Pizza!')
    pS = input('What size pizza would you like (S,M,L): ') #pizza Size
    pT = {} #pizza Toppings
    res = Pizza(pS,pT) #initalize pizza obj

    #while loop set up
    pT = input('Type topping to add (or Enter to quit): ')
    while pT != '':
        res.addTopping(pT)
        pT = input('Type topping to add (or Enter to quit): ')
        
    print('Thanks for ordering!')
    print(f'Your pizza costs ${res.price()}')
    return res

        
## doctest
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw8TEST.py'))
