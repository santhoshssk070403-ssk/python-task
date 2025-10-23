#1
def add(**a):
    for i in a.keys():
        print("key", i)
add(a=1,b=3,c="ssk",d=30)        



print("\n________****2****__________\n")



#2

def add(**a):
    for i in a.values():
        print("values is:", i)
add(a=1,b=3,c="ssk",d=30)        


print("\n________****3****__________\n")

#3

def add(**add):
    total = 0
    for i in add.values():
        total+= i
        print("sum of total value is:", total)
add(a=1,b=30,c=20,d=40)

print("\n________****4****__________\n")


#4
def add(**add):
    total =0
    print("the even numbers:")
    for i in add.values():
        if i % 2 == 0:
            print(i)
            total += i
    print("the sum number is :", total)
add(a=1,b=3,c=2,d=4,e=3,f=8,g=44,h=21)

print("\n________****6****__________\n")
        
#6
def number(*a):
    for i in a:
        div=[]
        for j in range(1,i):
            if i%j==0:
                div.append(j)
        sa=sum(div)
        if sa==i:
            print("its a perfect number")
        else:
            print("its a not perfect")
a=int(input("enter the num:"))            
b=int(input("enter the num:"))        
number(a,b)

print("\n________****7****__________\n")
#7
def last(**k):
    print("Original Dictionary:", k)
    if k:
        last = list(k.keys())[-1]
        k.pop(last)
        print("After removing last key ",last, k)
    else:
        print("Dictionary is empty!")
last(a=10, b=20, c=30)


print("\n________****8****__________\n")

#8
def cal(a, b, ope):
    if ope == '+':
        print(a + b == a + b)
    elif ope == '-':
        print(a - b == a - b)
    elif ope == '*':
        print(a * b == a * b)
    elif ope == '/':
        if b != 0:
            print(a / b == a / b)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator!")

cal(10, 5, '+')
cal(10, 5, '/')


print("\n________****8****__________\n")


#9
def cal():
      print("simple calculator")
      print("1. add \n, 2 sub \n, 3. multi \n 4. divi")
      choice=input("enter the choice 1-4 :")
      
      if choice in ['1', '2', '3', '4']:
          num1=float (input("enter the num:"))
          num2=float (input("enter the num :"))
          
          if choice=='1':
              print("add", numl+num2)
          elif choice=='2':
              print("sub", num1-num2)
          elif choice=='3':
              print("multi", num1*num2)
          elif choice=='4':
              if num2!=0:
                     print("divi", num1/num2)
              else:
                     print("error! divisable by zero")
          else:
               print("invalid choice")
cal()


print("\n________****10****__________\n")
#10


def palin(p):
    a=p.lower()
    rev=a[::-1]
    if a==rev:
        print("is a palindrome")
    else:
        print("not a palindrome")

m=input("enter the string:")
palin(m)    
        
print("\n________****11****__________\n")


#11

def count(s):
    vow=0
    conso=0
    spec=0
    for i in s:
         if i.isalpha():
             if i.lower() in 'aeiou':
                 vow+=1
             else:
                 conso+=1
         elif not i .isspace():
             spec+=1
    print("vowels:",vow ,"consonanats:",conso ,"special:",spec )
it=input("enter the string:")
count(it)
    
