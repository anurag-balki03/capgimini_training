class parent:
    def __init__(self):
        self.bignose="7CM"
        
    def display(self):
        print("in parent class")

class child(parent):
    def __init__(self):
        super().__init__()
        print("in child class")
        
ch=child()
ch.display()
print(ch.bignose)