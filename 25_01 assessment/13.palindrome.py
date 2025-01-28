def is_palindrome(num):
    sum=0
    temp=num
    rem=0
    while(num>0):
        rem=num%10
        sum=(sum*10)+rem
        num=int(num/10)
    if(sum==temp):
        print(f"YES {sum} IS A PALINDROME")
    else:
        print(f"{sum} IS NOT A PALINDROME")
    return

print("HELLO USER\n")
t=True
while(t):
    ch=int(input("CHOOSE AN OPTION \n1. GIVE A NUMBER \n2. EXIT\n"))
    if(ch==2):
        t=False
    else:
        number=int(input("ENTER THE NUMBER:"))
        is_palindrome(number)
