# d={}
# print("the empty dictionary: ",d)

# d={'spam': 1, 'eggs': 2}
# print("the two item dictionary: ",d)

# d={'food':{'ham': 1, 'eggs': 2}}
# print("the nested dictionary: ",d)

# d=dict(name='abc': age=40)
# print(d)

keylist=['spam', 'ham', 'eggs']
valist=[1, 60, 40, 4]
d=dict(zip(keylist,valist))
# print("the zipper: ",d)

# d=dict.fromkeys(['a','b'])
d2={'elephant': 10, 'cheetha': 5}
d.update(d2)
print("the updated dictionary: ",d)

list1=list(d.keys())
print("keys:",list1)

list1=list(d.values())
print("values:",list1)

a=d.get('elephant',4)
print("get key value: ",a)

