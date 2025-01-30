class management:
    def manage(self):
        self.name=input("enter the name of the student: ")
        self.unique_id=int(input("enter the unique id of the student:"))    
        self.fees=int(input("enter the academic fees of the student"))
        self.due=int(input("enter the library due if any else provide 0: "))
    
    def display(self):
        print(f"name of the student: {self.name}")
        print(f"unique id of the student: {self.unique_id}")
        print(f"the academic fees of the student: {self.fees}")
        print(f"the library due of the student: {self.due}")

class school(management):
    def __init__(self):
        print("in school")
        super.manage()
        super.display()
        
class ug:
    def __init__(self):
        print("in ug")
        super.manage()
        super.display()

class pg:
    def __init__(self):
        print("in pg")
        super.manage()
        super.display()

s=school()
u=ug()
p=pg()
