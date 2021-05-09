class Animal:

    def __init__(self, colour, sex, klass):
        self.colour = colour
        self.sex = sex
        self.klass = klass

class Neko(Animal):

    def __init__(self, colour, sex, klass, ear_size, fur, eye_colour):
        super(Neko, self).__init__(colour, sex, klass)
        self.ear_size = ear_size
        self.fur = fur
        self.eye_colour = eye_colour


class Dog(Animal):

    def __init__(self, colour, sex, klass, tail_size, paroda, size ):
        super(Dog, self).__init__(colour, sex, klass)
        self.tail_size = tail_size
        self.paroda = paroda
        self.size = size


n1 = Neko("grey", 'male', 'cats', 5, 'long', 'green')
d1 = Dog('black', 'female', 'dog', 10, 'bitbul', 'small')

print(d1.paroda)
print(n1.fur)
print(d1.tail_size)
print(n1.klass)
print(d1.eat())
