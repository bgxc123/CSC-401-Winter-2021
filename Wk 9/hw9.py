#Name: Brendan Gee
#Contributors:
#Sources:

#Stack#
class Stack(list):
    def __repr__(self):
        return f'Stack({list.__repr__(self)})'
    def push(self,item):
        self.append(item)
    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False

#parenthesesMatch#
def parenthesesMatch(s):
    res = Stack()
    
    for i in s:
        if i in '[{(':
            res.push(i)
        elif i in ']})' and len(res) == 0:
            return False
        elif i in ']})' and len(res) != 0:
            temp = res.pop()
            #not sure if there is a better way to do this lol
            if temp == '(' and i == ')' or temp == '[' and i == ']' or temp == '{' and i == '}':
                pass
            else:
                return False
    
                
    return res.isEmpty()
    
    



#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw9TEST.py'))
