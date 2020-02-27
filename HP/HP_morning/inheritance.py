class employee:
    def __init__(self,empID,empnm):
        self.empID = empID
        self.empnm = empnm
    def display(self):
        print("Name is",self.empnm,"Employee id is:",self.empID)
class manager(employee):
    def __init__(self,empID, empnm,cabinID):
        employee.__init__(self,empID,empnm)
        self.cabinID = cabinID
    def display(self):
        employee.display(self)
        print("Cabin ID is:",self.cabinID)

m1 = manager(101,"ABC",111)
m1.display()