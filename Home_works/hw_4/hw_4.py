
class Factorial:

    def __init__(self, num):
        self.num = num

    def fact(self):
        if self.num == 0:
            return 1
        else:
            temp_num = self.num
            self.num -= 1
            return temp_num * self.fact()


f = Factorial(9)
print(f.fact())
