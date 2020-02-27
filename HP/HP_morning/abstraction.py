#abstract class
class myclass:
    def calculate(self):
        pass

class subclass(myclass):
    def calculate(self, a):
        self.a = a
        print("square=",self.a*self.a)

class subclass1(myclass):
    def calculate(self, a):
        self.a = a
        print("cube is=",self.a*self.a*self.a)

s1 = subclass()
s2 = subclass1()
s1.calculate(10)
s2.calculate(2)