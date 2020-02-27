class bank:
    def __init__(self, name, ano, bal):
        self.name = name
        self.ano = ano
        self.__bal = bal
    def deposite(self,amt):
        self.__bal+=amt
    def withdraw(self,amt):
        self.__bal-=amt
    def display(self):
        print("Name is:",self.name)
        print("Acc no is:",self.ano)
        print("Balance is:",self.__bal)
        print(id(self.__bal))

b = bank("abc", 123, 1000)
b.display()
b.deposite(2000)
b.display()
b.withdraw(500)
b.display()
b.bal = 10000
b.display()
        