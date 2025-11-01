#1
try:
    a=float(input("enter the number:"))
    b=float(input("enter the number:"))
    c=a/b
except ZeroDivisionError:
        print("can't divided by 0")
except ValueError:
        print("please the enter the numbri value only")
else:
        print("diviosn",c)

        
print("\n________****2****_________\n")
#2
def add(a,b):
    try:
        return a+b
    except TypeError:
        print("input must in numbers" )
print("sum:",add (30,5))    

print("\n________****3****_________\n")

#3
try:
    a=int(input("enter a integer:"))
    print("valid integer entered:",a)
except ValueError as b:
    print("ValueError",b)
    
print("\n________****4****_________\n")
#4
try:
    a = input("Enter 1st number: ")
    b = input("Enter 2nd number: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numerical.")
    print("Valid numbers entered:", float(a), float(b))
except TypeError as e:
    print("TypeError:", e)

print("\n__________****5****____________\n")
#5'''

try:
    lst = [10, 20, 30, 40, 50]
    value = int(input("Enter value to search: "))
    if value not in lst:
        raise ValueError(value, "not found in the list")
    print(f"{value} found at index {lst.index(value)}")
except ValueError as e:
    print("Error:", e)

print("\n__________****6****____________\n")

