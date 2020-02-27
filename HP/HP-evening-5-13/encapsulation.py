# class myclass:
#     def __init__(self,a):
#         self.a = a
#     def display(self):
#         print("value for a is:",self.a)
# c = myclass(10)
# c.display()
# c.a = 30
# c.display()

class bank:
    def __init__(self,no,name,balance):
        self.no = no
        self.name = name
        self.__balance = balance
    def withdraw(self, amt):
        self.__balance = self.__balance - amt
    def deposite(self,amt):
        self.__balance = self.__balance + amt
    def display(self):
        print("Ac no is:",self.no)
        print("Name is:",self.name)
        print("Balance is:",self.__balance)
        print(id(self.no))
b = bank(100, "ABC", 2000)
b.display()
b.withdraw(500)
b.display()
b.deposite(1000)
b.display()
b.balance = 100000
b.no = 222
b.display()