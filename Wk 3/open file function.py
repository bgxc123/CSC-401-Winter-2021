def stringCount(file,string):
    infile = open(file,'r')
    obj = infile.read()
    infile.close()
    return obj.count(string)

            
def words(filename):
    infile = open(filename,'r')
    content = infile.read()
    infile.close()
    table = str.maketrans('!.,;:?',6*' ')
    content = content.translate(table)
    return content.split()
