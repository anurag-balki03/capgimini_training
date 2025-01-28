import dis

# def multiply(a,b):
#     m=a*b
#     return m

# a=2
# b=3
# res=multiply(a,b)
# dis.dis(multiply)
# print(f"value: {res}")

def test(n):
    for i in range(1,n):
        a=i
        print(a)

n=int(input("enter number: "))
test(n)
dis.dis(test)