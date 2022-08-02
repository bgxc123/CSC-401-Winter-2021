# LoopExamples.py

##### nonDecreasing #####

# called *sorted* in text
'''
A sequence of numbers is NON-DECREASING if
the numbers either increase or stay equal.

DETERMINE whether a given sequence of
numbers is non-decreasing:

>>> nonDecreasing( [2,3,3,4,5,7,9,10] )
True
>>> nonDecreasing( [2,3,3,4,1,5,7,9,10] )
False

SEARCH for a DECREASING consecutive pair.
If you find a decrease, return False. If
the loop completes, there were no
decreases, so return True.

Q: How do you iterate over the pairs?
A: INDEXED ITERATION!
'''

def nonDecreasing( numlst ):

    for i in range(len(numlst)-1):
        # if decrease
        if numlst[i]>numlst[i+1]:
            # print(i,numlst[i],numlst[i+1])
            return False
    # did not find a decrease
    return True

##### gcd #####
'''
compute the greatest common divisor of two given integers:

>>> gcd(15,21)
3
>>> gcd(60,84)
12
'''

# https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm

'''
(Elementary) Euclid's algorithm. For a,b>0:
gcd(a,a) = a
gcd(a,b) = gcd(a-b,b), if a>b
gcd(a,b) = gcd(a,b-a), if b>a
'''

def gcd(a,b):
    ''' Given positive integers a and b,
    return their greatest common
    divisor.'''
    print(a,b)
    while a!=b:

        # if a greater, subtract b
        if a>b:
            a -= b
        # if b greater, subtract a
        else:
            b -= a
        print(a,b)

    return a # or b! (they are equal)
            
'''
>>> gcd(15,21)
15 21
15 6
9 6
3 6
3 3
3
>>> gcd(410545,125784)
410545 125784
284761 125784
158977 125784
33193 125784
33193 92591
33193 59398
33193 26205
6988 26205
6988 19217
6988 12229
6988 5241
1747 5241
1747 3494
1747 1747
1747
>>> gcd(24,2)
24 2
22 2
20 2
18 2
16 2
14 2
12 2
10 2
8 2
6 2
4 2
2 2
2
>>>
'''















