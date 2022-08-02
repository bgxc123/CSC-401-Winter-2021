#PP 7.2#

#for each variable, identify if it is local or global

def f(y): #f is global, y is local
    x = 2 # local
    return g(x) 

def g(y): #g global, y local
    global x # x global
    x = 4 
    return x*y #x global, y local

x = 0 # global
res = f(x) #all global
print('x = {}, f(0) = {}'.format(x, res)) #x is global, res is global

#PP 7.3#
def safe(file, read):
    try:
        infile = open(file, read)
        return infile
    except:
        return None

#PP 8.1#
class Point:
    def setx(self,xcoord):
        self.x = xcoord
    def sety(self,ycoord):
        self.y = ycoord
    def get(self):
        return self.x,self.y
    def move(self,dx,dy):
        self.x += dx
        self.y += dy

#PP 8.2#
class Test:
    version = 1.02


###Animal Class
##class Animal:
##    def setSpecies(self,species):
##        self.s = species
##    def setLanguage(self,lang):
##        self.l = lang
##    def speak(self):
##        print('I am a {} and I {}'.format(self.s,self.l))

#PP 8.3#
class Rectangle:
    def setSize(self,w,l):
        self.w = w
        self.l = l
    def perimeter(self):
        return 2*(self.w + self.l)
    def area(self):
        return self.w * self.l
    
#PP 8.4#
class Animal:
    def __init__(self,s='animal',l='make sounds'):
        self.s = s
        self.l = l
    def speak(self):
        print('I am a {} and I {}'.format(self.s,self.l))
