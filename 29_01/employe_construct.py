class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_emp(self):
        print(f"list of employee: {self.name}")
        print(f"salaries of the employees: {self.salary}")

emp=employee(["AAA","BBB","CCC"],[10000,15000,8000])
emp.display_emp()