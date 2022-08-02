# hw4.py
# Name: Brendan Gee
#Collaborators:
#References:


#vowelIndex#
def vowelIndex(word):
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOU':
            return i
    return -1
        
#flipCase#
def flipCase(word):
    '''return uppercase lowercase & vice versa'''
    result = ''
    for i in word:
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()
    return result

#palindromes#

def palindromes(sentence):
    '''returns list of palindromes from a sentence'''
    nopunct = ''
    res = []
    for i in sentence: #getting rid of punctuation
        if i not in ";:,?!.":
            nopunct += i
    for word in nopunct.split():
        if word.lower() == word[::-1].lower():
            res.append(word)
    return res

#squares#

def squares(lst):
    '''counts total perfect squares in a 2d list'''
    res = 0
    for i in range(len(lst)): #obtains row index in 2d list
        for j in range(len(lst[i])): #obtains col index in 2d list
            #print(lst[i][j]) prints out each number
            for num in range(lst[i][j]+1): #checks if current iteration is a perfect square
                if num*num == lst[i][j]:
                    res+= 1
    return res
            
                   
#rps#
def rps(p1,p2):
    '''game of rock paper scissors'''
    if p1 == 'R' and p2 == 'P':
        return 1
    elif p1 == 'R' and p2 == 'S':
        return -1
    elif p1 == 'P' and p2 == 'S':
        return 1
    elif p1 == 'P' and p2 == 'R':
        return -1
    elif p1 == 'S' and p2 == 'R':
        return 1
    elif p1 == 'S' and p2 == 'P':
        return -1
    else:
        return 0

#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))


