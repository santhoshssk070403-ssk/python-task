import math
b1=int(input("enter a num:" ))
b2=int(input("enter a num:" ))
h=int(input("enter a num:"))
r=int(input("enter the radius:"))
trapex=((b1+b2)*h/2)

print("pi value:",math.pi*r**2)
print("trapexoid:",trapex)
print("cylinder:",math.pi*r**2*h)
print("sphere:",math.pi*r**2*4/3)
print("cone:",math.pi*r**3*1/3)

