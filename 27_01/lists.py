l1=[]
print("1. an empty list: ",l1)

l2=[0,1,2,3]
print(f"2. list with 4 items:{l2}")

l3=['abc',['def','ghi']]
print("3. a nested list: ",l3)

l4=list('spam')
print("4. list created form string 'spam': ",l4)

l5=list(range(4,-4,-1))
print("5. list created from range(-4 to 4)",l5)

l6=[10,20,30,40]
print("6. element at index 2: ",l6[::-1])

l7=['x',[10,20,30],'y']
print("7. element at l7[1][2]",l7[1][2])

l8=[0,1,2,3,4,5]
print("8. slicing l8 from index 2 to 4",l8[2:5])

l9=[10,[100,200,300,400],50]
print("9a. element at l9[1]: ",l9[1])
print("9b. element at l9[1][3]: ",l9[1][3])
print("9c. Slicing sublist l9[1][1:3]: ",l9[1][1:3])