# find the largest number using given number 542789

num = int(input("Enter the number: "))

lst = [int(d) for d in str(num)]

lst.sort(reverse=True)

print(int("".join(map(str,lst))))

print("--------------------------------------")


