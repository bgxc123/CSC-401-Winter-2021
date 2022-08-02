# WhileInput.py

##### user input using while #####
'''
make this work: 

>>> total = sumUserNums()
Enter a number: 23
Enter a number: 12.2
Enter a number: 1.5
Enter a number: 11
Enter a number: 
>>> total
47.7
'''
##### loop and a half pattern #####
# while, accumulator

def sumUserNums():

    total = 0
    ans = input('Enter a number: ') # half
    while ans != '':
        total += eval(ans)
        # ans is either a '##' or ''
        ans = input('Enter a number: ')
    return total      
  

##### infinite loop pattern #####

def sumUserNums():

    total = 0
    while True:
        # ans is either a '##' or ''
        ans = input('Enter a number: ')
        if ans =='':
            break # stop the loop
        else: # '##'
            total += eval(ans)
    return total

# c,C++,Java - do while *NOT in Python*
















