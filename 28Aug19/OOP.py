class Myclass:
    #name = ""
    def display(abc,name):
        abc.name=name
        print("{}".format(abc.name))
    def display2(self):
        #print("This is Python class")
        print("{}".format(self.name))
class Myclass2:
    def display2(self):
        #print("This is Python class")
        print("{}".format(self.name))

o1=Myclass()
#o1.name="GNS Technologies"
#o1.display("python")
#o1.name="Python"
o1.display2()

