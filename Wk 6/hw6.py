#hw 6#
#Name: Brendan Gee
#Contributors:
#Sources:

#interleaved#

def interleaved(lst1,lst2):
    res = []
    i = 0
    j = 0
    #checking both lists for the smallest num
    while i < len(lst1) and j < len(lst2):
        if lst1[i] >= lst2[j]:
            res.append(lst2[j])
            j += 1
        else:
            res.append(lst1[i])
            i += 1
    #appending the remains of the list
    res += list(lst1[i:]) + list(lst2[j:]) #list function for the ranges
            
    return res
                                                  
#primeFac#

def primeFac(num):
    res = []
    while num > 1:
        for i in range(2,num+1):
            if num % i == 0:
                res.append(i)
                num = int(num / i)
                break
        else:
            continue
    return res

#piggybank#

def piggyBank(lst):
    coinSum = 0
    res = {'Q': 0, 'D': 0, 'N':0, 'P':0}
    for i in lst:
        res[i] += 1
    coinSum += 25*res['Q'] + 10*res['D'] + 5*res['N'] + 1*res['P']
    return res, coinSum

#craps#
import random
def craps():
    #first roll
    roll1 = random.randrange(1,7) + random.randrange(1,7)
    if roll1 in [7,11]:
        return 1
    elif roll1 in [2,3,12]:
        return 0

    #second roll
    while True:
        nextRoll = random.randrange(1,7) + random.randrange(1,7)
        if roll1 == nextRoll:
            return 1
        if nextRoll == 7:
            return 0

#testCraps#

def testCraps(num):
    res = []
    for i in range(num):
        res.append(craps())
    return sum(res) / num

#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py'))
