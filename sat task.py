#1
print("\n____________*****1****______________\n")

a= {'a': 1, 'b': 2, 'c': 3}
key = input("enter the value:")
if key in a:
    print(f" Key '{key}' exist in the dictionary.")
else:
    print(f" key '{key}'not exist .")
    
    
    

print("\n____________*****2****______________\n")



#2
a = {'a': 1, 'b': 2, 'c': 3}

for key, value in a.items():
    print(f"Key: {key}, Value: {value}")


print("\n____________*****3****______________\n")

#3
squares = {x: x**2 for x in range(1, 16)}
print(squares)


print("\n____________*****4****______________\n")

#4
di1 = {'a': 10, 'b': 20}
di2 = {'c': 30, 'd': 40}

merge = {**di1, **di2}
print(merge)


print("\n____________*****5*****______________\n")

#5

di1 = {'a': 100, 'b': 200, 'c': 300}
total = sum(di1.values())
print("Sum of values:", total)


print("\n____________*****6*****______________\n")

#6

di1={'a':1,'b':2,'c':3}
result = 1
for i in di1.values():
      result *=i
print("multiply of dict",result)      


print("\n____________*****7*****______________\n")

#7
di1 = {'a': 1, 'b': 2, 'c': 3}
remove= di1.popitem()
print("Updated dictionary:", di1)


print("\n____________*****8*****______________\n")

#8

di1 = {'a': 1, 'b': 2, 'c': 3}
size=len(di1)
print("size of the given value:",size)



print("\n____________*****9*****______________\n")

#9
emp = ['sankaruu', 'rasabba', 'rajeshuu']
defaults = {'designation': 'Developer', 'salary': 50000}

empdict = dict.fromkeys(emp, defaults)
print(empdict)


print("\n____________*****10*****______________\n")


#10

di1 = {'name': 'subuninee', 'age': 25, 'city': 'New York', 'gender': 'Male'}
extract = ['name', 'city']

di2 = {k: di1[k]
       for k in extract}
print(di2)

print("\n____________*****11*****______________\n")

#11

my_dict = {'a': 1, 'b': 2}
print("Type of my_dict:", type(my_dict))

