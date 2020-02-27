"""class AccessControl:
    __a = 0
    def __init__(self, a):
        self.__a = a
    def display(self):
        print("a:",self.__a)

o1 = AccessControl(10)
o1.display()
o1.__a = 100
o1.display()"""


#Bank account
class Bank:
    def __init__(self, name, no, balance):
        self.name = name
        self.no = no
        self.__balance = balance

    def deposit(self, amt):
        self.__balance = self.__balance + amt 
    def withdraw(self, amt):
        self.__balance = self.__balance - amt
    def showbalance(self):
        print("name is:",self.name)
        print("ac no:",self.no)
        print("Balance is:",self.__balance)
        print(id(self.__balance))
b1 = Bank("ABC",123,1000)
b1.showbalance()
b1.deposit(2000)
b1.showbalance()
b1.withdraw(500)
b1.showbalance()
b1.balance = 2000
b1.showbalance()



