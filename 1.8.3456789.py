# greatest common divison
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

def simple_fraction(fraction):
    common = gcd(fraction.num,fraction.den)
    fraction.num = fraction.num // common
    fraction.den = fraction.den // common
    return fraction


class Fraction:
    def __init__(self, top, bottom):
        if top and bottom is int:
            self.num = top
            self.den = bottom
        else:
            raise Exception('please enter int')

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        #self_common = gcd(self.num, self.den)
        #self.num = self.num//self_common
        #self.den = self.den//self_common

        #otherfraction_common = gcd(otherfraction.num,
         #                   otherfraction.den)
        #otherfraction.num = otherfraction.num//otherfraction_common
        #otherfraction.den = otherfraction.den//otherfraction_common
        self = simple_fraction(self)
        otherfraction = simple_fraction(otherfraction)

        newnum = self.num * otherfraction.den + \
                    self.den * otherfraction.num
        newden = self.den * otherfraction.den
        
        return Fraction(newnum, newden)

    def __sub__(self,otherfraction):
        self = simple_fraction(self)
        otherfraction = simple_fraction(otherfraction)

        newnum = self.num * otherfraction.den - \
                        self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

       

    def __mul__(self,otherfraction):
        self = simple_fraction(self)
        otherfraction = simple_fraction(otherfraction)
        
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __truediv__(self,otherfraction):
        self = simple_fraction(self)
        otherfraction = simple_fraction(otherfraction)
         
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num

        return Fraction(newnum, newden)

#deep equal: a and b is equal and a b is different object
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

#less than
    def __lt__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum < secondnum

#less and equal than
    def __le__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum <= secondnum

#great than
    def __gt__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum

#great and equal
    def __ge__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum >= secondnum

#not equal
    def __ne__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum != secondnum

a = Fraction(0.3,9)
b = Fraction(2,8)
print('print a and b:')
print(a)
print(b)
a.show()
b.show()

print('print a+b ')
print(a.__add__(b))
print(a+b)

print('print a==b')
print(a.__eq__(b))
print(a==b)

print('print a*b')
print(a.__mul__(b))
print(a*b)

print('print a-b')
print(a.__sub__(b))
print(a-b)

print('print b-a')
print(b.__sub__(a))
print(b-a)

print('print a/b')
print(a.__truediv__(b))
print(a/b)

print('print b/a')
print(b.__truediv__(a))
print(b/a)

print('print a>b')
print(a.__ge__(b))
print(a>b)

print('print a>=b')
print(a.__gt__(b))
print(a>=b)

print('print a<b')
print(a.__lt__(b))
print(a<b)

print('print a<=b')
print(a.__le__(b))
print(a<=b)

print('print a!=b')
print(a.__ne__(b))
print(a!=b)
