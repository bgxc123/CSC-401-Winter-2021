def interest(rate):
    n = 0
    while (1+rate)**n < 2:
        n+=1
    return n

#loop & a half statement
def cities():
    lst = []
    city = input('Enter city: ')
    while city != '':
        lst.append(city)
        city = input('Enter city: ')
    return lst

#infinite loop statement
def cities():
    lst = []
    while True:
        city = input('Enter city: ')
        if city != '':
            lst.append(city)
        else:
            return lst
