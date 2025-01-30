class destructorex:
    def __init__(self,name):
        print(f"object {self.name} is created.")
    def __del__(self):
        print(f"object is destroyed")
obj=destructorex("sample")
del obj