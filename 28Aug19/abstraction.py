'''from abc import ABC, abstractmethod
class Myclass(ABC):
    def calculate(self):
        pass

class subclass(Myclass):
    def calculate(self, x):
        self.x = x
        print("square of no is:",x*x)
class subclass1(Myclass):
    def calculate(self, x):
        print("cube of no is:",x*x*x)
s = Myclass()
s.calculate()
s1 = subclass()
s1.calculate(4)
s2 = subclass1()
s2.calculate(5)'''


from abc import *
class employee(ABC):
    def salary(self):
        pass

class developer(employee):
    def salary(self, basic):
        self.basic = basic
        hra = basic*0.1
        print("hra is:", hra)
        print("gross salary is",basic+1000+hra)

class manager(employee):
    def salary(self, basic):
        self.basic = basic
        hra = basic*0.2
        print("hra is:",hra )
        print("gross salary is",basic+2000+hra)

d1 = developer()
d1.salary(2000)
m1 = manager()
m1.salary(5000)
