
# n=int(input("enter the range: "))
# for i in range(n):
#     num=int(input("ente the value: "))
#     ll.append(num)
numbers=[int(input(f"enter the value for{i+1}")) for i in range(5)]
res=sum(numbers)
print(f"the sum of the given inputs: {res}")