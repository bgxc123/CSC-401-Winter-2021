# hw2.py
# Name: Brendan Gee
#Collaborators:
#References: 

#3.23(f)
def forLoops():
    for i in range(5,22,4):
        print(i)

#3.34
def pay(wage,hours):
    '''function calculates employees
    pay in prev week'''
    if hours <= 40:
        return wage * hours
    else:
        return (wage*40) + (1.5*wage)*(hours - 40)

#3.38
def abbreviation(dayOfweek):
    '''function returns two letter abbreviation
        for day of the week'''
    if dayOfweek in 'MondayTuesdayWednesdayThursdayFridaySaturdaySunday':
        return dayOfweek[0:2]
 
#3.39
import math #need sqrt function
def collision(x1,y1,r1,x2,y2,r2):
    '''Checks if 2 circular objects collide'''
    if math.sqrt((x1-x2)**2)+math.sqrt((y1-y2)**2) > r1 + r2:
        '''checks if distance from center to center
            is greater than distance of both radius'''
        return False
    else:
        return True
#3.40
def partition(lst):
    '''Splits a list into 2 groups'''
    for i in lst:
        if i[0] in 'ABCDEFGHIJKLM':
            print(i)

#3.41
def lastF(FirstName,LastName):
    '''Returns 2 strings in form 'LastName, F.' '''
    return LastName + ', '+FirstName[0] + '.'

#doctest
if __name__=='__main__':
   import doctest
   print( doctest.testfile('hw2TEST.py'))
