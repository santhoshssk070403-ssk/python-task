#1
a=["1,2,3,4,5,6,7"]
a.append("8")
print(a)


print("\n----------------*****2*****-----------------\n")


#2
a=("apple","orange","graps","mango")
for i in a:
      print(i)



print("\n----------------*****3*****-----------------\n")

#3
names = []
while True:
    name = input("Enter a name (type 'stop' to end): ")
    if name.lower() == "stop":
        break
    names.append(name)
print("List of names:", names)

print("\n----------------*****4*****-----------------\n")

#4

num= [1,2,3]
for i in [4,5,6]:
      num.append(i)
print("the updated list is:",num)      


print("\n----------------*****5*****-----------------\n")

#5
city = ["Mad", "Chen", "Coimb", "Salem", "Tri"]
print("Original list:", city)
city.remove("Salem")
print("After removing 'Salem':", city)


print("\n----------------*****6*****-----------------\n")

#6
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num[:]:
    if i % 2 == 0:
        num.remove(i)
print("After removing even numbers:", num)


print("\n----------------*****7*****-----------------\n")


#7
subjects = []
for i in range(5):
    sub = input("Enter subject name: ")
    subjects.append(sub)
print("Subjects list:", subjects)



print("\n----------------*****8*****-----------------\n")

#8
it = ["pen", "pencil", "book", "eraser", "scale"]
print("Current items:", it)
remove = input("Enter the item to remove: ")
if remove in it:
    it.remove(remove)
    print("After removing:", it)
else:
    print("Item not found in list!")

print("\n----------------*****9*****-----------------\n")

#9
numbers = []
for i in range(1, 11):
    numbers.append(i)
print("Numbers list:", numbers)


print("\n----------------*****9*****-----------------\n")

#10


num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num2 in num1[:]:
    if num2 % 2 == 0:
        num1.remove(num2)
print("After removing even numbers:", num1)
