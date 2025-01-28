#factorial program

def factorial(rang):
    fact=1
    for i in range(2,rang+1):
        fact *= i
        print(fact)
    return


rang=int(input("enter the range: "))
if(rang<0):
    print("negative range")
    rang=int(input("enter a positive value: "))
# elif(rang==1):
#     print(1)
# elif(rang==2):
#     print(1)
#     print(2)
else:
    print(1)
    factorial(rang)
    