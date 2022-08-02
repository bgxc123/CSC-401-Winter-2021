def Celsius(f):
    x = 5/9*(f-32)
    return x
def Login(ID):
    if ID in ['joe', 'sue', 'hani', 'sophie']:
        print('You are in!')
    else:
        print('unknown')
    print('Done!')
    
def average(x,y):
    return (x+y)/2
def noVowel(word):
    x = True
    for i in word:
        if i.lower() in 'aeiou':
            x = False
        else:
            break
    return x

def allEven(list):
    for i in list:
        if i % 2 != 0:
            return False    
    return True
def negatives(int):
    'lists all the negative numbers in a list'
    for i in int:
        if i < 0:
            print(i)


            
