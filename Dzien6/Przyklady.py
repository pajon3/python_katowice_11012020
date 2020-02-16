class Square:
    def __init__(self,a):
        self.a = a

    @property
    def area(self):
        return self.a ** 2

s1 = Square(3)
s2 = Square(4)

print(s1+s2h )