# RandomDictExamples.py

##### random example #####
'''
make this work: simulate a dice game
where you roll 2 dice, keep rolling as
long as you roll doubles.  return the
total number of pips rolled:  e.g.

3 3
5 5
2 1

return 19

>>> diceTotal() # for above rolls
19
'''

import random
# accumulator, while
def diceTotal(): # no paramters
    pips = 0
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    pips += die1 + die2
    #print( die1, die2)
    while die1==die2:
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        pips += die1 + die2
        #print( die1, die2)
    return pips

'''
>>> [diceTotal() for i in range(20)]
[5, 4, 7, 8, 12, 3, 8, 7, 7, 9, 6, 10, 8, 5, 7, 15, 7, 9, 19, 13]
>>> games = [diceTotal() for i in range(1000)]
>>> from Dictionaries import frequencies
>>> frequencies( games )
{8: 124, 4: 57, 5: 112, 7: 150, 11: 66, 9: 115, 12: 14, 6: 114, 3: 62, 10: 69, 18: 12, 13: 17, 15: 18, 21: 7, 32: 1, 16: 13, 14: 11, 17: 10, 25: 4, 20: 6, 23: 4, 19: 9, 26: 1, 22: 1, 28: 1, 31: 1, 51: 1}
>>>
'''

##### another dict problem #####

'''
Write a function encode that will
translate any characters in a given
dictionary (and leave others alone)

>>> d = {'a':'k', 'b':'g'}
>>> encode( 'bat', d )
'gkt'
'''

def encode( phrase, d ):
    # accumulate a str
    ans = ""
    # iterate over the phrase
    for char in phrase:
        # if letter in dictionary
        # replace it
        if char in d:
            ans += d[char]
        # otherwise, dont
        else:
            ans += char
    return ans

'''
>>> d = {'a':'k', 'b':'g'}
>>> encode( 'bat', d )
'gkt'
>>>


'''


##### substitution cipher #####
'''
Encode a message by replacing each letter
in the alphabet with another letter in the
alphabet.

>>> alphabet = 'abcdefghijklmnopqrstuvwxyz'
>>> alpha2 = list( alphabet )
>>> alpha2
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> random.shuffle(alpha2)
>>> alpha2
['o', 'a', 'v', 'z', 'g', 'h', 'i', 'q', 'k', 'n', 'j', 'm', 'u', 'd', 'x', 'c', 'r', 's', 'y', 'p', 't', 'w', 'l', 'b', 'f', 'e']
>>> alphabet = list(alphabet)
>>> alphabet
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> zip( alphabet, alpha2 )
<zip object at 0x000001FEFD77BD48>
>>> list( zip( alphabet, alpha2 ) )
[('a', 'o'), ('b', 'a'), ('c', 'v'), ('d', 'z'), ('e', 'g'), ('f', 'h'), ('g', 'i'), ('h', 'q'), ('i', 'k'), ('j', 'n'), ('k', 'j'), ('l', 'm'), ('m', 'u'), ('n', 'd'), ('o', 'x'), ('p', 'c'), ('q', 'r'), ('r', 's'), ('s', 'y'), ('t', 'p'), ('u', 't'), ('v', 'w'), ('w', 'l'), ('x', 'b'), ('y', 'f'), ('z', 'e')]
>>> dict( zip( alphabet, alpha2 ) )
{'a': 'o', 'b': 'a', 'c': 'v', 'd': 'z', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'q', 'i': 'k', 'j': 'n', 'k': 'j', 'l': 'm', 'm': 'u', 'n': 'd', 'o': 'x', 'p': 'c', 'q': 'r', 'r': 's', 's': 'y', 't': 'p', 'u': 't', 'v': 'w', 'w': 'l', 'x': 'b', 'y': 'f', 'z': 'e'}
>>> code = dict( zip( alphabet, alpha2 ) )
>>> encode('the quick red fox jumped over the lazy brown dog', code)
'pqg rtkvj sgz hxb ntucgz xwgs pqg moef asxld zxi'
>>> 

''' 


##### exercise:DECODE this message! #####
'''
This message was encoded with a
substitution cipher.  Try to decode it!
'''

msg = '''
>>> aitmjx xwan
Xwl Flc mo Texwmc, qe Xai Tlxljn

Qlksxaosu an qlxxlj xwkc srue.
Lztuayax an qlxxlj xwkc aituayax.
Naitul an qlxxlj xwkc ymitulz.
Ymitulz an qlxxlj xwkc ymituaykxlh.
Oukx an qlxxlj xwkc clnxlh.
Ntkjnl an qlxxlj xwkc hlcnl.
Jlkhkqauaxe ymscxn.
Ntlyaku yknln kjlc'x ntlyaku lcmsrw xm qjlkb xwl jsuln.
Kuxwmsrw tjkyxaykuaxe qlkxn tsjaxe.
Ljjmjn nwmsuh cldlj tknn naulcxue.
Sculnn lztuayaxue naulcylh.
Ac xwl okyl mo kiqarsaxe, jlosnl xwl xlitxkxamc xm rslnn.
Xwljl nwmsuh ql mcl-- kch tjloljkque mcue mcl --mqdamsn vke xm hm ax.
Kuxwmsrw xwkx vke ike cmx ql mqdamsn kx oajnx sculnn ems'jl Hsxyw.
Cmv an qlxxlj xwkc cldlj.
Kuxwmsrw cldlj an moxlc qlxxlj xwkc *jarwx* cmv.
Ao xwl aitulilcxkxamc an wkjh xm lztukac, ax'n k qkh ahlk.
Ao xwl aitulilcxkxamc an lkne xm lztukac, ax ike ql k rmmh ahlk.
Ckilntkyln kjl mcl wmcbacr rjlkx ahlk -- ulx'n hm imjl mo xwmnl!
'''

code = { 'O':'f'}
msg = msg.upper()
print( encode(msg,code) )

'''

>>> AITMJX XWAN
XWL FLC Mf TEXWMC, QE XAI TLXLJN

QLKSXAfSU AN QLXXLJ XWKC SRUE.
LZTUAYAX AN QLXXLJ XWKC AITUAYAX.
NAITUL AN QLXXLJ XWKC YMITULZ.
YMITULZ AN QLXXLJ XWKC YMITUAYKXLH.
fUKX AN QLXXLJ XWKC CLNXLH.
NTKJNL AN QLXXLJ XWKC HLCNL.
JLKHKQAUAXE YMSCXN.
NTLYAKU YKNLN KJLC'X NTLYAKU LCMSRW XM QJLKB XWL JSULN.
KUXWMSRW TJKYXAYKUAXE QLKXN TSJAXE.
LJJMJN NWMSUH CLDLJ TKNN NAULCXUE.
SCULNN LZTUAYAXUE NAULCYLH.
AC XWL fKYL Mf KIQARSAXE, JLfSNL XWL XLITXKXAMC XM RSLNN.
XWLJL NWMSUH QL MCL-- KCH TJLfLJKQUE MCUE MCL --MQDAMSN VKE XM HM AX.
KUXWMSRW XWKX VKE IKE CMX QL MQDAMSN KX fAJNX SCULNN EMS'JL HSXYW.
CMV AN QLXXLJ XWKC CLDLJ.
KUXWMSRW CLDLJ AN MfXLC QLXXLJ XWKC *JARWX* CMV.
Af XWL AITULILCXKXAMC AN WKJH XM LZTUKAC, AX'N K QKH AHLK.
Af XWL AITULILCXKXAMC AN LKNE XM LZTUKAC, AX IKE QL K RMMH AHLK.
CKILNTKYLN KJL MCL WMCBACR RJLKX AHLK -- ULX'N HM IMJL Mf XWMNL!

>>> # msg is in English
>>> # certain letters are more frequent
>>> from Dictionaries import frequencies
>>> frequencies( msg )
{'\n': 23, '>': 3, ' ': 126, 'A': 55, 'I': 17, 'T': 23, 'M': 44, 'J': 34, 'X': 81, 'W': 32, 'N': 47, 'L': 92, 'F': 1, 'C': 42, 'O': 12, 'E': 17, ',': 4, 'Q': 21, 'K': 53, 'S': 21, 'U': 33, 'R': 11, '.': 18, 'Z': 6, 'Y': 17, 'H': 17, "'": 4, 'B': 2, 'D': 5, '-': 6, 'V': 4, '*': 2, '!': 1}
>>>
'''

