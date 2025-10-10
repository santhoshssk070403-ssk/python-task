s=int(input("enter a num:"))
fact=1

if s<0:
    print("invalid")

elif s ==1:
    print("the fact of 0 is 1")


else:
    for i in range (1,s+1):
        fact *= i
        print("the factorial of",s,"is",fact)
    
    
