class employee:
    def __init__(self,name,empID):
        self.name = name
        self.empID = empID
    def display(self):
        print("Name is:",self.name,"Employee id is:",self.empID)

class manager(employee):
    def __init__(self, name, empID, CabinID):
        employee.__init__(self,name,empID)
        self.CabinID = CabinID
    def display(self):
        employee.display(self)
        print("Cabin ID is:",self.CabinID)

m1 = manager("ABC", 101, 222)
m1.display()
    