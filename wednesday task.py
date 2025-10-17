#1
a="sa nth osh"
b=a.replace(" ","-")
print(b)

#2
print("\n-------------******2******---------------\n")



a="python123"
print(a[3 : -3])


#3
print("\n-------------*******3*****---------------\n")


a="santhosh kumar"
b=list(a)
b[0]=b[0].upper()
b[-1]=b[-1].upper()
c=' '.join(b)
print(c)


#4
print("\n-------------*******4*****---------------\n")


a=input("enter the word:")
b=len(a)
print("the lenght of the Text:",b)

#5
print("\n-------------*******5*****---------------\n")

a=input("enter the words:")
b=a.startswith("a")
print(b)


#6
print("\n-------------********6****---------------\n")


a=input("enter the words:")
b=a.endswith("ing")
print(b)
#


#7
print("\n-------------*******7*****---------------\n")


a=input("Enter the words:")
b=a.replace("a","-")
print(b)


#8
print("\n-------------*******8*****---------------\n")



a=input("Enter the word:")
b=a.find("a")
print(b)

#9
print("\n-------------*******9*****---------------\n")

a=input("Enter the word:")
b=a.isalnum()
print(b)


#10
print("\n-------------*******10*****---------------\n")



a= input("Enter a string: ")
b= " "

for char in a:
    b = char + b  
print("The reversed string is:", b)
    
    
