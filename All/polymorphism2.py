"""class myclass:
    name = ""
    def display(self,name):
        self.name=name
        print(self.name)
    def show():
        print("This is Python class")


o1=myclass()
o1.display("Python")
o1.show()"""

class Rectangle:
    def __init__(self,height=10,width=20):
        self.height=height
        self.width=width
        area = self.height*self.width
        print("area of rectangle is",area)

r1=Rectangle(20,30)
print(r1.height)
print(r1.width)




