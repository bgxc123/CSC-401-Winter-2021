#HW2
def loop():
    for i in range(5,22,4):
        print(i)

def pay(wage, hours):
    if hours <= 40:
        return wage * hours
    else:
        return wage * 40 + wage*(1.5*(hours - 40))

def abbreviation(day):
    if day in 'MondayTuesdayWednesdayThursdayFriday':
        return day[0:2]

import math
def collision(x1,y1,r1,x2,y2,r2):
    if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1+r2:
        return True
    else:
        return False

def partition(lst):
    for i in lst:
        if 'A' <= i <= 'M':
            print(i)

##def lastF(FirstName,LastName):
##    return LastName +', '+ FirstName[0] + '.'
##
##PP4.1#
