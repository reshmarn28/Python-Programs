#initializer
"""class Rectangle:
    height = 0
    base = 0
    def __init__(self):
        self.height=0
        self.base=0
        print("__init__ method")
    def display(self):
        print("__init__ method2")
r1=Rectangle()
r1.display()"""

#parameterized initializer
"""class Rectangle:
    
    def __init__(self,height=None,base=40):
        self.height = height
        self.base = base
        print("__init method__")
r1=Rectangle()
print(r1.height)
print(r1.base)"""

#constructor with parameters
class Rectangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def display(self):
        print("height is:{}".format(self.height))
        print("base is:{}".format(self.base))
    def area(self):
        a = self.height * self.base
        print("area is:",a)
r1 = Rectangle(10,20)
r1.display()
r1.area()

