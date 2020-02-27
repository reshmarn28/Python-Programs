# class my_class:
#     def display(self,name,age):
#         self.name=name
#         self.age=age
#         print("My name is"+self.name+" My age is",self.age)
# c1=my_class()
# c1.display("Sunny",25)

# class myclass:
#     name = ""
#     def display(abc):
#         print("Welcome"+abc.name)
# c1=myclass()
# c1.name="Python"
# c1.display()

# class rectangle:
#     height = 0
#     base = 0
#     def __init__(self):
#         self.height = 0
#         self.base = 0
#         print("init method",self.height)
#     def display(self):
#         print("Welcome")
# r1=rectangle()
# r1.display()

class rectangle:
    def __init__(self,height,base):
        self.height = height
        self.base = base
        print("Height is:",self.height,"base is:",self.base)
    def area(self):
        area = self.height*self.base
        return area
r1 = rectangle(10,20)
print("area is:",r1.area())
