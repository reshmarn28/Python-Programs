# class my_class:
#     str = ""
#     def display(self):
#         print("Welcome to OOPs")
#         print(self.str+"is easy")
# c1 = my_class()
# c1.display()
# c1.str = "Python"
# c1.display()


class myclass:
    def __init__(self,height=10,base=20):
        self.height = height
        self.base = base
        print("__init method__")
    def display(self):
        print(self.height)
c1 = myclass()
print(c1.height)
print(c1.base)
c1.display()