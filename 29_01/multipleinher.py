class man:
    def describe_m(self):
        return "man is a male gender"

class women:
    def describe_w(self):
        return "a women is a female gender"
    
class kid:
    def describe_k(self):
        return "kid goes to school"

class school(kid):
    def truth(self):
        return "kid came to school"
    
class person(man,women,kid):
    def per_son(self):
        return "every person is a human"
    

per=person()
print(per.describe_m())
print(per.describe_w())
print(per.describe_k())

m=man()
m=per
print(m.per_son())
print("******************")
sc=school()
print(sc.describe_k())
print(sc.truth())
