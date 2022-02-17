from stack import Stack
rStack = Stack()

def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr(n // base, base)

print(toStr(10,2))
