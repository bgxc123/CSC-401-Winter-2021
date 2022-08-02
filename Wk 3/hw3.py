# hw3.py
# Name: Brendan Gee
#Collaborators:
#References:

#4.24#
def cheer(string):
    print('How do you spell winner?')
    print('I know, I know!')
    #for loop to iterate over each letter to get caps & space using end
    for i in string:
        print(i.upper(),end=' ')
    # '!' for the end of the last phrase, \n for new line
    print("!\nAnd that's how you spell winner!")
    print('Go {}!'.format(string))
       
#4.25#
def vowelCount(string):
    '''Counts total vowels in a given string'''
    a = string.count('a'.lower())
    e = string.count('e'.lower())
    i = string.count('i'.lower())
    o = string.count('o'.lower())
    u = string.count('u'.lower())
    print('''a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times.'''.format(a,e,i,o,u))
    
#4.26#
def crypto(filename):
    infile = open(filename,'r')
    content = infile.read()
    infile.close()
    
    print(content.replace('secret','xxxxxx'))
    
#4.28#
def links(filename):
    '''Counts # of links in html file'''
    infile = open(filename, 'r')
    content = infile.readlines()
    infile.close()
    linkcount = 0
    for i in content:
        if '</a>' in i:
            linkcount+=1
    return linkcount
#4.31#
def duplicate(filename):
    '''checks for duplicate word in a file '''
    infile = open(filename, 'r')
    #replace to remove punctuation
    content = infile.read().lower().replace('.','').replace(',','').split()
    infile.close()
    for i in content:
        if content.count(i) == 1:
            pass
        else:
            return True
    #return function outside for loop *only* when we check for no duplicates
    return False

#doctest
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))
        
