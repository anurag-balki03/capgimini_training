def big(new,temp,var,tvar):
    if(new>temp):
        return new,tvar
    else:
        return temp,var

def getin():
    a=int(input("enter number 1: "))
    temp=a
    var='a'
    b=int(input("enter number 2: "))
    tvar='b'
    temp,var=big(b,temp,var,tvar)
    c=int(input("enter number 3: "))
    tvar='c'
    temp,var=big(c,temp,var,tvar)
    d=int(input("enter number 4: "))
    tvar='d'
    temp,var=big(d,temp,var,tvar)
    return a,b,c,d,temp,var

# def find_large(a,b,c):
#     if(a>b and a>c):
#         return a,'a'
#     elif (b>c):
#         return b,'b'
#     else:
#         return c,'c'

def display(data,var):
    den=10
    print(f"{var} is the largest ie {data} {den}")

(a,b,c,d,great,var)=getin()
# sum,var=find_large(a,b,c)
display(great,var)
