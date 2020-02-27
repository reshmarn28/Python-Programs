#from abc import ABC
class calc():
    def __calculate(self):
        print("abc")
class calc1(calc):
    def calculate(self,a):
        self.a = a
        print("sq is:",self.a * self.a)
class calc2(calc):
    def calculate(self,a):
        self.a = a
        print("cube is:",self.a*self.a*self.a)
c = calc()
c.calculate()
c1 = calc1()
c1.calculate(10) 
c2 = calc2()
c2.calculate(20)   
        
    