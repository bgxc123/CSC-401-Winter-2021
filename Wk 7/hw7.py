#Name: Brendan Gee
#Contributors:
#Sources:

#Volume#
class Volume:
    #initialize object at default value 0
    def __init__(self,v=0):
        self.v = v
        if self.v > 11:
            self.v = 11
        elif self.v < 0:
            self.v = 0
    #instead of indicating the namespace of an obj, return a string
    def __repr__(self):
        return f'Volume({self.v})'
    #ability to use boolean operators when comparing different values
    def __eq__(self,other):
        if self.v == other.v:
            return True
        else:
            return False
    #change the volume     
    def set(self,num):
        if num > 11:
            num = 11
        elif num < 0:
            num = 0
        self.v = num
    #return the volume int
    def get(self):
        return self.v
    #add given value to self.v
    def up(self,dv):
        if self.v + dv > 11:
            self.v = 11
        else:
            self.v += dv
    #subtract given value to self.v       
    def down(self,dv):
        if self.v - dv < 0:
            self.v = 0
        else:
            self.v -= dv

#partyVolume#
def partyVolume(file):
    infile = open(file, 'r')
    
    #get first line and the rest of the lines
    firstVol = float(infile.readline().replace('\n',''))
    restOfvol = infile.readlines()
    infile.close()
    
    #convert firstVol to Volume object
    res = Volume(firstVol)

    #logic to determine if vol should go up/down using class Volume methods
    for i in restOfvol:
        if i[0].upper() == 'D':
            res.down(float(i[2:-1]))
        else:
            res.up(float(i[2:-1]))
    return res

#wow this last prob was trickyyyy....


#doctest#
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw7TEST.py'))
