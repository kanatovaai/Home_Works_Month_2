class Complex_numbers():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_numbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex_numbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex_numbers(self.real * other.real, self.imag * other.imag)

    def __truediv__(self, other):
        return Complex_numbers(self.real * other.imag, self.imag * other.real)

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
