class dept:
    comp = "Some Company"
    def __init__(self,deptID=6969,deptName='Python'):
        self.deptID = deptID
        self.deptName=deptName

    def display(self):
        print(f"{self.deptName} has ID {self.deptID}")

if __name__=='__main__':
    obj1 = dept()
    obj1.display()
    print(obj1.comp)

    