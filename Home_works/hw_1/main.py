
class Fraction:

    def __init__(self, num,  denom):
        self.num = num
        self.denom = denom




    def add(self, other):
        num = self.num * other.denom + self.denom * other.num
        denom = self.denom * other.denom
        print(num)
        print('-')
        print(denom)


    def divide(self, other):
        num = self.num * other.denom
        denom = self.denom * other.num
        print('---------------------')
        print(num)
        print('-')
        print(denom)

    def multiply(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        print('---------------------')
        print(num)
        print('-')
        print(denom)

    def subtract(self, other):
        num = self.num * other.denom - self.denom * other.num
        denom = self.denom * other.denom
        print('---------------------')
        print(num)
        print('-')
        print(denom)

f1 = Fraction(10, 5)
f2 = Fraction(20, 5)
f1.add(f2)
f1.divide(f2)
f1.multiply(f2)
f1.subtract(f2)


