
##numCapitalized
def numCapitalized(s):
    '''count number of words with a capital letter'''
    counter = 0
    for i in s.split():
        for j in i:
            if j == j.upper():
                counter += 1
                break
    return counter
##gct gallons/cups/tablespoons
#source for conversions: https://www.goodcooking.com/conversions/tea_gall.htm
## 256 tbsp in a gal, 16 tbsp in a cup
def gct(tbsp):
    '''returns a string with # of gallons/cups/tbsps in integer'''
    g = str(tbsp // 256) + 'g,'
    c = str(tbsp % 256 // 16) +'c,'
    t = str(tbsp % 256 % 16 // 1) + 't'
    if len(g) == 3:
        g = '0' + g
    if len(c) == 3:
        c = '0' + c
    if len(t) == 2:
        t = '0' +t
    TTL = g + c + t
    return TTL

##priceTShirt
def priceTShirt(size, slogan):
    '''computes and returns price of T-Shirt'''
    cost = 0
    if size == 'S':
        cost+= 12
    elif size == 'M':
        cost+= 15
    else:
        cost += 18
    for i in slogan:
        if i in (".,!'\"?:'"):
            cost += .20
        elif i in (' \n'):
            cost += 0
        elif i == i.upper():
            cost += .30
        elif i == i.lower():
            cost += .25
    return cost
        
##altercase
def alterCase(s):
    res = ''
    for i in range(len(s)):
        if i % 2 == 0:
            res += s[i].upper()
        else:
            res += s[i].lower()
    return res

## doctest
if __name__=='__main__':
    import doctest
    print( doctest.testfile('midtermPracticeTEST.py'))


    
