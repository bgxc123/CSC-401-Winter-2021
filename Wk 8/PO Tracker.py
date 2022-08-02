def PO_String():
    infile = open('PO Test.csv', 'r')
    content = infile.readlines()
    infile.close()
    res = ''
    i = 0
    while i < len(content):
        res += "'" + content[i].replace('\n','') + "';,"
        i += 1
    res += "'" + content[-1].replace('\n','') + "'"
    return res

def PO_STR(num):
    infile = open('PO Test.csv', 'r')
    content = infile.readlines()
    infile.close()
    res = ''
    for i in range(len(content)):
        if i < num+1:
            print(content[i],i, end=' ')
        else:
            print('\n'+content[i])
            i = 0
