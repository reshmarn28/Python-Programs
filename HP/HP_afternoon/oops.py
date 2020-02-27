class cat:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name+"is eating")
class dog:
    def __init__(self, name):
        self.name = name
    def eat(self,age):
        print(self.name+"is eating")
        print(age)

def feedanimal(animal):
    animal.eat()

c = cat("cat")
d = dog("dog")
feedanimal(d)
feedanimal(c)