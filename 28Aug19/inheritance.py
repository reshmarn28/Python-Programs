class employee:
    def __init__(self, name, empID):
        self.name = name
        self.empID = empID
    def display(self):
        print("name is:{}".format(self.name))
        print("empID is:{}".format(self.empID))
class manager(employee):
    def __init__(self,name,empID,cabinID):
        self.cabinID = cabinID
        employee.__init__(self, name, empID)
    def display(self):
        print("cabin Id is:{}".format(self.cabinID))
        employee.display(self)
class developer(manager):
    def __init__(self,name,empID,cabinID,tableno):
        self.tableno = tableno
        manager.__init__(self,name,empID,cabinID)
    def display(self):
        manager.display(self)
        print("table no is:{}".format(self.tableno))
d1 = developer("XYZ", 201, 222, 333)
d1.display()
