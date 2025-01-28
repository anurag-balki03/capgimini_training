def getin():
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    c=int(input("enter number 3: "))
    d=int(input("enter number 4: "))
    return(a,b,c,d)

def findsum(p,q,r,s):
    res=p+q+r+s
    return res

def findavg(sum):
    res=sum/4
    return res

def display(data):
    print(f"average of 4 numbers is: {data}")

(p,q,r,s)=getin()
sum=findsum(p,q,r,s)
data=findavg(sum)
display(data)