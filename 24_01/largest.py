def getin():
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    c=int(input("enter number 3: "))
    return a,b,c

def find_large(a,b,c):
    if(a>b and a>c):
        return a,'a'
    elif (b>c):
        return b,'b'
    else:
        return c,'c'
def display(data,var):
    print(f"{var} is the largest ie {data},")

(a,b,c)=getin()
sum,var=find_large(a,b,c)
display(sum,var)
