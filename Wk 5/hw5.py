#hw 5#
#Name: Brendan Gee
#Contributors:
#Sources:

#doubleVowel#
def doubleVowel(s):
    for i in range(len(s)-1):
        if s[i].lower() in 'aeiou' and s[i+1].lower() in 'aeiou':
            return True
    return False

#numPairs#
def numPairs(target, numlst):
    res = 0
    for i in range(len(numlst)):
        # need to check for each index in lst with ith index for the target
        for j in range(i+1,len(numlst)):
            if numlst[i] + numlst[j] == target:
                res += 1
    return res

#hideshow#
def hideShow(s,m):
    res = ''
    for i in range(len(m)):
        if m[i] == '0':
            res +='#'
        else:
            res += s[i]
    return res

#clean#
def clean(s):
    i = 0
    res = ''
    #leading space characters
    while s[0] in ' \n\t':
        s = s[1:]
    while s[-1] in ' \n\t':
        s = s[:-1]
    return s

#sequence#
def sequence(num):
    print(num)
    while num != 1:
        if num % 2 == 1:
            num += 1
            print(num)
        else:
            num = int(num/2)
            print(num)

#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))
