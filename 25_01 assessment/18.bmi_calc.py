import math

def bmi_calculator(weight,height):
    res=weight/(height**2)
    print(res)
    if(res<18.5):
        print("underweight")
    elif(res>=18.5 and res<24.9):
        print("normal weight")
    elif(res>=24.9 and res<29.9):
        print("overweight")
    else:
        print("obesity")
        
weight=float(input("enter the weight in kgs: "))
height=float(input("enter the height of the person in mts: "))
bmi_calculator(weight,height)