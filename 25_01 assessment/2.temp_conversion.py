#2. Celsius, Fahrenheit, and Kelvin conversion 
def get_input():
    value=float(input("enter the temparature "))
    return value

def celsius_to_fahrenheit():
    temp=get_input()
    new_temp=temp*9/5+32
    print(f"the converted temparature {temp}C to {new_temp}F")
    
def celsius_to_kelvin():
    temp=get_input()
    new_temp=temp+273.15
    print(f"the converted temparature {temp}C to {new_temp}K")
    
def Fahrenheit_to_Celsius():
    temp=get_input()
    new_temp=(temp-32)*5/9
    print(f"the converted temparature {temp}F to {new_temp}C")
    
def Fahrenheit_to_Kelvin():
    temp=get_input()
    new_temp=(temp-32)*(5/9)+273.15
    print(f"the converted temparature {temp}F to {new_temp}K")
    
def Kelvin_to_Celsius():
    temp=get_input()
    new_temp=temp-273.15
    print(f"the converted temparature {temp}K to {new_temp}C")
    
def Kelvin_to_Fahrenheit():
    temp=get_input()
    new_temp=(temp-273.15)*(9/5)+32
    print(f"the converted temparature {temp}K to {new_temp}F")
    
def switch(ch):
    if(ch==1):
        celsius_to_fahrenheit()
        return
    elif(ch==2):
        celsius_to_kelvin()
        return
    elif(ch==3):
        Fahrenheit_to_Celsius()
        return
    elif(ch==4):
        Fahrenheit_to_Kelvin()
        return
    elif(ch==5):
        Kelvin_to_Celsius()
        return
    elif(ch==6):
        Kelvin_to_Fahrenheit()
        return
    else:
        print("INVALID OPTION \n")
        return

print("HELLO USER \n")
ch=int(input("PLEASE ENTER THE TYPE OF CONVERSION YOU ARE LOOKING FOR \n1.celsius_to_fahrenheit \n2.celsius_to_kelvin \n3.Fahrenheit_to_Celsius \n4.Fahrenheit_to_Kelvin \n5.Kelvin_to_Celsius \n6.Kelvin_to_Fahrenheit \n"))
switch(ch)