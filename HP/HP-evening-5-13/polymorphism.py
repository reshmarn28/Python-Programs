class cat:
    def __init__(self,name):
        self.name=name
    def eat(self,age):
        self.age = age
        print(self.age)
    def eat(self):
        print(self.name+"is eating")

class dog:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name+"is eating")

def feedanimal(animal):
    animal.eat()

c1 = cat("cat")
d1 = dog("doggy")
# feedanimal(c1)
# feedanimal(d1)
c1.eat(12)
c1.eat()


