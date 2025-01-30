class parent:
    def display(self):
        print("in parent class")

class child(parent):
    def __init__(self):
        print("in child class")
        
ch=child()
ch.display()
