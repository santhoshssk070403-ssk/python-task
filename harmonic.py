n = int(input("Enter the number of terms: "))

harmonic= 0

print("Harmonic Series:")
for i in range(1, n + 1):
    harmonic += 1 / i
    print("1/{i}", end=" ")
    if i != n:
        print("+", end=" ")

print("\n Sum of harmonic series up to" , harmonic)
