class Complex_Numbers():

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex_Numbers(self.real + other.real, self.img + other.imag)

    def __sub__(self, other):
        return Complex_Numbers(self.real - other.real, self.img - other.imag)

    def __mul__(self, other):
        return Complex_Numbers(self.real * other.real, self.img * other.imag)

    def __truediv__(self, other):
        return Complex_Numbers(self.real * other.imag, self.img * other.real)

c1 = complex(11, 11)
c2 = complex(2, 2)
c3 = complex(56, 89)
c4 = complex(24, 5)
add = c1 + c2 + c3 + c4
print(add)
sub = c1 - c2 - c3 - c4
print(sub)
# f = complex(2, 1)
# g = complex(2, 1)
# mul = f * g
# print(mul)
mul = c1 * c2 * c3 * c4
print(mul)
truediv = c1 / c2 / c3 / c4
print(truediv)
f = complex(2, 1)
g = complex(2, 1)
truediv = f / g
print(truediv)
