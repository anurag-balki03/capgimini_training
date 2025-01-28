# list1=[]
# list1.append(list(input("enter the string: ")))
# list2=list1[::-1]
# print(f"string:{list1}")
# print(f"reversed string: {list2}")
string=input()
lst=list(string)
if lst==lst[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
