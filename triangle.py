t1 = int(input("Enter length of first side: "))
t2= int(input("Enter length of second side: "))
t3= int(input("Enter length of third side: "))

if (t1 + t2 > t3) and (t1 + t3 > t2) and (t2 + t3> t1):
    if t1== t2 == t3:
        print("_____The triangle is Equilateral____.")
    elif t1 == t2 or t2 == t3 or t1 ==t2:
        print("_____The triangle is Isosceles_____.")
    else:
        print("____The triangle is Scalene_____.")
else:
    print("The given sides do not form a valid triangle.")
