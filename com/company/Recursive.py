# Print from N to 1

def Print(n):
    if n == 0:
        return
    print(n)
    return Print(n - 1)


n = int(input("Enter the number: "))
output = Print(n)

print("-------------------------------------")


# sum from 1 to N

def sum_1_To_N(num):
    if num == 1:
        return 1

    ans = num + sum_1_To_N(num - 1)
    return ans


n = int(input("Enter the number: "))
output1 = sum_1_To_N(n)
print("The sum from 1 to N is: ", output1)

print("-------------------------------------")


# Print from 1 to N

def Print_1_To_N(n):
    if n == 0:
        return
    Print_1_To_N(n - 1)
    print(n)


n = int(input("Enter the number: "))
Print_1_To_N(n)

print("-------------------------------------")


def fibonacci(Num, a=0, b=1):
    if Num > 0:
        print(a, end=" ")

        fibonacci(Num - 1, b, a + b)


n = int(input("Enter the number: "))
fibonacci(n)
print()

print("-------------------------------------")


# Factor for number
def Factor_for_number(number, i=1):
    if i > number:
        return
    if n % i == 0:
        print(i, end=" ")
    Factor_for_number(n, i + 1)


n = int(input("Enter the number: "))
Factor_for_number(n)

print()

print("-------------------------------------")


def power(a, b):
    if b == 0:
        return 1

    ans = a * power(a, b - 1)
    return ans


a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
res = power(a, b)
print(res)

print("-------------------------------------")


def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


fib_num = int(input("Enter the number for fib: "))
# nn = fib(fib_num)
# print(nn)
# for list
for i in range(1, n + 1):
    print(i)
