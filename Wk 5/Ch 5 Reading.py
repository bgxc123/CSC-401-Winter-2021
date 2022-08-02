#CH 5 Reading

#PP 5.1#
def myBMI(weight,height):
    res = (weight*703) / (height**2)
    if res < 18.5:
        print('Underweight')
    elif res < 24.5:
        print('Normal')
    else:
        print('Overweight')

#PP 5.2#
def powers(n):
    for i in range(1,n+1):
        print(2**i, end = ' ')

#PP 5.3#
def arithmetic(numlst):
    if len(numlst) < 2:
        return True
    diff = numlst[1] - numlst[0]
    for i in range(len(numlst)-1):
        if numlst[i+1] - numlst[i] != diff:
            return False
    return True

#PP 5.4#
def factorial(num):
    res = 1
    if num == 0:
        return res
    for i in range(1,num+1):
        res *= i
    return res

#PP 5.5#
def acronym(s):
    res = ''
    s = s.split()
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j == 0:
                res += s[i][j].upper()
    return res

#PP 5.7#
def xmult(lst1,lst2):
    res = []
    for i in lst1:
        for j in lst2:
            res.append(i*j)
    return res

#PP 5.8#
def bubbleSort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

#PP 5.9#
def add2D(t,s):
    for i in range(len(t)):
        for j in range(len(t[i])):
            s[i][j]+= t[i][j]
    return s

#PP 5.10#
def interest(rate):
    t = 1
    while (1+rate)**t < 2:
        t+=1
    return t

#PP 5.11#
def approxE(error):
    prev = 1
    cur = 2
    i = 2
    while cur - prev > error:
        prev = cur
        cur = prev + 1/factorial(i)
        i += 1
    return cur

def cities():
    lst = []
    city = input('Enter city: ')
    while city != '':
        lst.append(city)
        city = input('Enter city: ')
    return lst

def cities2():
    lst = []
    while True:
        city = input('Enter city: ')
        if city == '':
            return lst
        lst.append(city)

