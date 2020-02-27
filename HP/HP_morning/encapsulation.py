# class encap:
#     def __init__(self, a):
#         self.__a = a
#     def display(self):
#         print(self.__a)
# o1 = encap(10)
# o1.display()
# o1.a = 100
# o1.display()

class bank:
    def __init__(self, name, no, bal):
        self.name = name
        self.no = no
        self.__bal = bal
    def withdraw(self, amt):
        self.__bal = self.__bal - amt
    def deposit(self, amt):
        self.__bal = self.__bal + amt
    def display(self):
        print("name is:",self.name,"ac no is:",self.no,"balance is:",self.__bal)
        print(id(self.__bal))
b = bank("abc",101,1000)
b.withdraw(500)
b.display()
b.deposit(2000)
b.display()
b.bal = 5000
b.display()