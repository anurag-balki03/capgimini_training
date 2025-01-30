class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        
    def allowances(self):
        self.allowance1=int(input("enter the allowances for food:"))
        self.allowance2=int(input("enter the allowances for stay:"))
        self.allowance3=int(input("enter the allowances for travel:"))
        return self.allowance1+self.allowance2+self.allowance3
    
    def deduction(self,salary):
        self.deduct=int(3/100)*salary
        print(f"tax deducted from salary: {self.deduct}")
        return self.deduct
        
    def set_salary(self,salary):
        self._salary=salary
    
    def get_salary(self):
        return self._salary+self.allowances()-self.deduction(self._salary)

    def get_name(self):
        return self._name
    
    def increment(self):
        self.new_sal=int(input("enter the updated salary:"))
        return self.new_sal

emp=employee("BOB",5000)
print(f"the initial salary of {emp.get_name()} {emp.get_salary()}")
emp.set_salary(emp.increment())
print(f"the updated salary of {emp.get_name()} {emp.get_salary()}")