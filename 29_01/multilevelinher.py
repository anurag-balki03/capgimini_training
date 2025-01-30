class cycle:
    def display_1(self):
        return "using cycle"

class bike(cycle):
    def display_2(self):
        return "using bike after cycle"

class car(bike):
    def display_3(self):
        return "usinig car after bike after cycle"

cr=car()
print(cr.display_1())
print(cr.display_2())
print(cr.display_3())
