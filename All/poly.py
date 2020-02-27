class dog:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("{} is eating".format(self.name))

class cat:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("{} is eating".format(self.name))

def feedanimal(animal):
    animal.eat()

d = dog("tommy")
c = cat("mani")

feedanimal(d)
feedanimal(c)