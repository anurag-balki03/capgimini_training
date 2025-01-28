import random

guess=random.randrange(1,100)
t=True
while(t):
    number=int(input("enter the number you guessed:"))
    diff=abs(guess-number)
    if(diff==0):
        print("you found the number")
        t=False
    elif(diff>=90):
        print("far away from the number")
    elif(diff>=80 and diff<90):
        print("you came a step ahead from the longest")
    elif(diff>=70 and diff<80):
        print("the distance is shrinking try a bit close")
    elif(diff>=50 and diff<80):
        print("try something less you came near")
    elif(diff>=30 and diff<50):
        print("close")
    elif(diff>=10 and diff<30):
        print("that was too close")
    elif(diff<10):
        print("you are almost there")
    else:
        continue
        