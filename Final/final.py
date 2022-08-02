#Final#
#Name: Brendan Gee
#Sources:

#differ#
def differ(s1,s2):
    res = 0
    for i in range(len(s1)):
        if s1[i].upper() != s2[i].upper():
            res +=1
    return res

#wordsByStart#
def wordsByStart(s):
    d = {}
    sentence = s.replace('.','').replace(',','').replace(';','').replace('!','').replace('?','').replace(':','').split()
    #print(sentence)
    for i in sentence:
        for j in i: #want to check the first letter j in each ith word
            if j.upper() not in d:
                d[j.upper()] = [i]
                break #break out of loop after checking first letter
            elif j.upper() in d:
                d[j.upper()].append(i)
                break #break out of loop after checking first letter
    return d
            
#vial#
class Vial:
    def __init__(self,brand,doses):
        self.brand = str(brand)
        self.doses = doses
    def __repr__(self):
        return f"Vial('{self.brand}',{self.doses})"
    def dose(self):
        if self.doses > 0:
            self.doses -= 1
            return self.brand
        else:
            return ''
    def getDoses(self):
        return self.doses
    def __eq__(self,other):
        return self.doses == other.doses
    def __gt__(self,other):
        return self.doses > other.doses

#rollDoubles#
import random
def rollDoubles():
    roll1 = random.randrange(1,7) #returns rand int in range 1 to 7 excl 7
    roll2 = random.randrange(1,7)
    roll = [roll1,roll2]
    #print(roll)
    counter = 2 #already rolled twice
    while roll[0] != roll[1]:
        if roll[0] > roll[1]:
            roll[1] = random.randrange(1,7)
            counter += 1
            #print(roll)
        elif roll[0] < roll[1]: #when second roll larger, swap indexes and roll smallest
            roll[0],roll[1] = roll[1],random.randrange(1,7)
            counter += 1
            #print(roll)
    return (sum(roll),counter)
            
        

#doctest#
if __name__ == '__main__':
    import doctest
    print( doctest.testfile('finalTEST.py'))
