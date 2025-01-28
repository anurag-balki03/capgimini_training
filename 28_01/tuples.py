t=()
print(f"the empty tuple: {t}")

t=(0,)
print(f"the tuple with one item: {t}")

t=(0,'ni',1.2,3)
print(f"the tuple with four items: {t}")

t=0,'ni',1.2,3
print(f"the tuple with four items: {t}")

t1=('abc',('def','ghi'))
print(f"the nested tuple: {t1}")

t=tuple('spam')
print(f"the convertion from string: {t}")

print(f"the t[1] term: {t[1]}")

print(f"the t[0][1] term: {t1[0][1]}")

print(f"terms 0 to 2: {t[0:3]}")

print("length of tuple",len(t))