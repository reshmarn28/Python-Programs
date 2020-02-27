# class encap:
#     def __init__(self,a):
#         self.__a = a
#     def display(self):
#         print("a is:",self.__a)
# e1=encap(30)
# e1.a = 20
# e1.display()
        

class Bank:
    def __init__(self,acno,name,bal):
        self.acno = acno
        self.name = name
        self.bal = bal
    def withdraw(self,amt):
        self.bal-=amt
    def deposite(self, amt):
        self.bal+=amt
    def display(self):
        print("name is:",self.name)
        print("account no is:",self.acno)
        print("balance is:",self.bal)
        print(id(self.bal))

b1 = Bank(101,"abc",1000)
b1.display()
b1.deposite(2000)
b1.display()
b1.withdraw(500)
b1.display()
b1.bal = 4000
b1.display()
print(b1.bal)

