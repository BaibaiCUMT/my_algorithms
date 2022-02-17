a = '3/5'
b = '13/15'
c = '1.5/3.5'
d = '12345/6789'
list = [a,b,c,d]

def getNum(semicolon_count):
    Num = semicolon_count.split('/')[0]
    print('%s num is %s'%(semicolon_count,Num))

def getDen(semicolon_count):
    Den = semicolon_count.split('/')[1]
    print('%s den is %s'%(semicolon_count,Den))

for i in list:
    getNum(i)
    getDen(i)
    print(' ')
