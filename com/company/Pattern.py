n = int(input("Enter n: "))

for i in range(n):
    print("*" * 5)
# what to print *
print("--------------------------------------------------")

for _ in range(n):
    for i in range(1, n+1):
        print(i, end=" ")
    print()

print("--------------------------------------------------")

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("--------------------------------------------------")

for i in range(1, n+1):     #loop for rows
    #printing spaces
    print(" " * (n-i), end="")
    #printing numbers
    for j in range(1, 2 * i):
        print(j, end="")
    print()
