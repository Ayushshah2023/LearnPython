class Parent:
    x=1
class Parent1:
    z=1
class Parent2:
    y=2
class Child(Parent1,Parent2):#multiple inheritance
#the order of the inheritance defines priority
#inheritance
    pass
p= Parent()
print(p.x)
c=Child()
print(c.z)
print(c.y)



class Parent:
    x=1
class Parent1:
    x=1
class Parent2:
    x=2
class Child(Parent1,Parent2):#multiple inheritance
#the order of the inheritance defines priority
#inheritance
    x=3
p= Parent()
print(p.x)
c=Child()
print(c.x)
print(c.x)
print(c.x)

