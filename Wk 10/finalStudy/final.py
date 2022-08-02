#sentencesByLength#
def sentencesByLength(filename):
    infile = open(filename, 'r')
    content = infile.read()
    content = content.replace('\n',' ')
    sentences = content.split('.')
    infile.close()
    res = {}
    for i in sentences:
        i = i.strip()
        n = len(i.split())
        #print(n,sentence)

        if n == 0:
            continue
        elif n in res:
            res[n].append(i.strip()+'.')
        else:
            res[n] = [i.strip()+'.']
    return res

#RandomCode#
import random
class RandomCode:
    def __init__(self, num, s):
        self.num = num
        self.s = ''
        counter = 0
        while counter < self.num:
            self.s += random.choice(s)
            counter+=1
            
    def __repr__(self):
        return f"RandomCode('{self.s}')"
    
    def getSecret(self):
        return self.s
    
    def getHint(self):
        return '?'* self.num
    
    def correct(self,string):
        if string == self.s:
            return True
        else:
            return False
        
    def correctPositions(self, num):
        res = 0
        for i in range(len(num)):
            if num[i] == self.s[i]:
                res +=1
        return res
    
    def correctLetters(self,string):
        res = []
        for i in string:
            for j in range(len(self.s)): #want to store position of j
                if j not in res: #ignore if position j already recorded
                    if i == self.s[j]:
                        res.append(j)
                        break
        return len(res)

def guessCode(n,g):
    r = RandomCode(n,g)
    print(f'Try to guess my secret code: {r.getHint()} (QUIT to stop)')
    print()
    counter = 0
    guess = input('What is your guess?: ')
    while guess != 'QUIT':
        if guess == r.getSecret():
            counter+=1
            print(f'Congratulations, you got it in {counter} guesses!')
            break
        else:
            print(f'Your guess has {r.correctLetters(guess)} correct letters, {r.correctPositions(guess)} in the correct position.\n')
            counter +=1
            guess = input('What is your guess?: ')
    if guess == 'QUIT':
        print()
        print(f'You gave up after {counter} guesses. ')
        print(f'The secret code is {r.getSecret()}.')

#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile('finalTEST.py'))
        
            
