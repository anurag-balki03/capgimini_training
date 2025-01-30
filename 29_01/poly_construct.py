class cat:
    def __init__(self):
        print("in class cat")
    
    def sound(self):
        print("MEOW")
class dog:
    def __init__(self):
        print("in class dog")
    
    def sound(self):
        print("BARk")
        
for animal in [cat(),dog()]:
    animal.sound()
