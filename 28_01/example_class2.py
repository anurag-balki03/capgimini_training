class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        self.allowances=int(input("enter the allowances:"))
    def set_salary(self,salary):
        self._salary=salary
    
    def get_salary(self):
        return self._salary+self.allowances

    def get_name(self):
        return self._name
    
    def increment(self):
        self.new_sal=int(input("enter the updated salary:"))
        return self.new_sal

emp=employee("BOB",5000)
print(f"the initial salary of {emp.get_name()} {emp.get_salary()}")
emp.set_salary(emp.increment())
print(f"the updated salary of {emp.get_name()} {emp.get_salary()}")