#Dictionaries are basically user defined indexes
#keys can be any type as long as it is immutable
#values can be any type
#dictionaries are mutable, like lists
# days['Fr'] = 'friday' -> changes the value in dict days/adds friday

#PP 6.1#
def birthState(key):
    d = {'Barack Hussein Obama II':'Hawaii', 'George Walker Bush':'Connecticut', 'William Jefferson Clinton':'Arkansas', 'George Herbert Walker Bush':'Massachussetts', 'Ronald Wilson Reagan':'Illinois',
'James Earl Carter, Jr':'Georgia'}
    return d[key]

#in and not in check if the KEY is in the dict

#PP 6.2#
def rlookup(d):
    while True:
        number = input('Enter phone number in the format (xxx)xxx-xx-xx: ')
        if number in d:
            return d[number]
        else:
            print('The number you have entered is not in use.')

#pop is the only shared method between list and dict.
##takes a key and pops a key,value pair

#update takes a dictionary as an input and adds/changes values in og dict

#for loop iterates over keys by default
##can specify d.values() for iterating over values
## d.items() returns tuple key,value pair

#PP 6.3#
def frequency(lst):
    d = {}
    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    return d

#PP 6.4#
def wordCounts(text):
    text = text.replace('','')
    d = {}
    for i in text.split():
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    for i in d:
        if d[i] == 1:
            print(i + f'  appears {d[i]} time.')
        else:
            print(i + f'  appears {d[i]} times.')

#while lists cannot be used as keys, tuples can to circumvent that issue
        
#PP 6.5#
def lookup(d):
    while True:
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        person = (first_name,last_name)
        if person in d:
            return d[person]
        else:
            print('The name you have entered is not in this dict.')
#randrange takes two numbers, and picks a rand int in that range
#PP 6.9#
import random
def guess(num):
    r = random.randrange(0,num)
    while True:
        g = int(input('Enter your guess: '))
        if g > r:
            print('Too high.')
        elif g < r:
            print('Too low.')
        else:
            print('You got it!')
            break

#random.uniform takes two numbers and returns a rand float in that interval
#random.shuffle => shuffles a random list
#random.choice => pulls a random char in an input string
  
