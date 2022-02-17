# greatest common divison
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                    self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

#deep equal
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

a = Fraction(1,3)
b = Fraction(1,4)
print(a)
print(b)

a.show()
b.show()

print(a.__add__(b))
print(a+b)
print(a.__eq__(b))
print(a==b)
