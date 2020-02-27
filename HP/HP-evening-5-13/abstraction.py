class myclass:
    def calculate(self):
        pass
class square():
    def calculate(self, a):
        self.a = a
        print("square of",self.a,"is:", self.a * self.a)

class cube():
    def calculate(self,a):
        self.a = a
        print("cube of",self.a,"is:",self.a * self.a*self.a)
class add():
    def calculate(self, a,b):
        self.a = a
        self.b = b
        print(self.a + self.b)
def maths(meth):
    meth.calculate(a,b)
    
o1 = square()
o2 = cube()
o3 = add()

maths(o1)
o1.calculate(4)
maths(o3)
o3.calculate(10,20)