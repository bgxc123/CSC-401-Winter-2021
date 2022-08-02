# Files.py

##### FILES #####
'''
Use Python to manipulate TEXT files.

open( filename,mode='r' )
    - opens a FILE with name filename
      and returns file object
    - file is relative to working folder
    - easiest to place in current folder

modes
    'r'ead - the default
    'w'rite
    'a'ppend

file methods:

    read() - returns contents as a str

    readlines() - returns a list of strs
    (one str per LINE)

    readline() - read a SINGLE line

    write(s) - writes a single str to file

    close() - closes the file, should
    always do this

3 STAGES:

    1) open file
    2) read(s)/write(s)
    3) close file (unless using with)

>>> # open the file
>>> infile = open('in.txt','r')
>>> infile
<_io.TextIOWrapper name='in.txt' mode='r' encoding='cp1252'>
>>> contents = infile.read()
>>> contents
"This is a file\nwith some text in it.\nIsn't that great?\n"
>>> infile.close()
>>> 
>>> contents.count('i')
6
>>> # read as lines
>>> infile = open('in.txt')
>>> lines = infile.readlines()
>>> infile.close()
>>> lines
['This is a file\n', 'with some text in it.\n', "Isn't that great?\n"]
>>> 
>>> 
>>> # write to a file
>>> # MUST specify 'w'rite
>>> outfile = open('out.txt','w')
>>> outfile.write('hello')
5
>>> outfile.write('how are you?')
12
>>> x = 9
>>> outfile.write( x )
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    outfile.write( x )
TypeError: write() argument must be str, not int
>>> outfile.write( str(x) + " is the answer" )
15
>>> outfile.close()
>>> 
>>> open('out.txt').read()
'hellohow are you?9 is the answer'
>>> 
'''

##### with statement #####
'''
instead of 3 stages: 

file = open('filename',mode='?')
... manipulate (read/write) file ... 
file.close()

USE with and only need 2!

with open('filename',mode='?') as file: 
    .... manipulate (read/write) file ... 
    # file CLOSES AUTOMATICALLY
'''

##### Example 1 #####
'''
make this work:
>>> numchars('out.txt')
???
'''

#v1 - a bit verbose
def numchars(filename):

    # open the file
    infile = open(filename,'r')
    # read contents
    contents = infile.read()
    # close the file
    infile.close()
    # count the characters
    # and return the answer
    return len(contents)

#v2 - very short, did NOT close file!
def numchars(filename):
    return len( open(filename,'r').read() )

#v3 - WITH automatically CLOSES file
def numchars(filename):
    with open(filename) as infile:
        return len(infile.read())
        # close file automatically


##### Example 2 #####

# read CSV (comma separated values)
# Excel file

'''
want this to work:
>>> getCell(3,2,'spreadsheet.csv')
5
'''

def getCell(row,col,filenameCSV):
    ''' returns the contents of the cell
    (row,col) of filenameCSV, uses 0-based
    indices'''
    with open('spreadsheet.csv') as infile:
        return eval( infile.readlines()[row].split(',')[col] )

     
# see pandas - Python Data Analysis Library
# for much more POWERFUL interaction with Excel




















