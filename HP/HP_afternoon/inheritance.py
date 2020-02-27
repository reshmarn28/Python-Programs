class emp:
    def __init__(self,ename,eno):
        self.ename = ename
        self.eno = eno
    def display(self):
        print("name is:",self.ename)
        print("emp id is:",self.eno)
class manager(emp):
    def __init__(self,ename,eno,cabinID):
        emp.__init__(self,ename,eno)
        self.cabinID = cabinID
    def display(self):
        emp.display(self)
        print("cabin id is:",self.cabinID)

m1 = manager("abc", 111, 202)
m1.display()
        