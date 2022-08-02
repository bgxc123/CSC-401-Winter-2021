# midterm.py
# Name: Brendan Gee
#References:




#piggybank#
def piggyBank(lst):
    coinsum = 0
    for i in lst:
        if i == 'Q':
            coinsum += 25
        elif i == 'D':
            coinsum +=10
        elif i == 'N':
            coinsum +=5
        elif i == 'P':
            coinsum +=1
        else:
            coinsum += 0
    return coinsum

#odds#
def odds(lst):
    oddnums = []
    for i in lst:
        for j in i:
            if j % 2 == 1:
                oddnums.append(j)
    return oddnums

#findWordOfLength#
def findWordOfLength(length, string):
    string = string.replace('.','').replace(',','').replace(';','').replace('!','').replace('?','').split()
    for i in range(len(string)):
        if len(string[i]) == length:
            return i
    return -1

#taller#
def taller(h1,h2):
    s1 = h1.replace('in','').replace('ft','')
    s2 = h2.replace('in','').replace('ft','')
    #checking for string length 2 => add a zero in the middle index
    if len(s1) == 2:
        s1 = s1[:1] + '0' + s1[1:]
    if len(s2) == 2:
        s2 = s2[:1] + '0' + s2[1:]
    if s1[0] > s2[0]:
        return h1
    elif s1[1:] > s2[1:]:
        return h1
    else:
        return h2
    
             

#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile('midtermTEST.py'))
