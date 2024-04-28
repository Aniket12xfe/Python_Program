# Problems on numbers

# num = int(input("Enter the number: "))
num = 12321
num = str(num)
num1 = num[::-1]

if num == num1:
    print("Palindrome number")
else:
    print("Not Palindrome")

print("------------------------------------")

# find Palindrome range of numbers

def checkPalindrome(num2):
    return str(num2) == str(num2)[::-1]

def MinMaxPalindrome(minimum, maximum):
    palindrome_number = []
    for i in range(minimum, maximum + 1):
        if checkPalindrome(i):
            palindrome_number.append(i)
    return palindrome_number

# mini = int(input("Enter minimum: "))
# maxi = int(input("Enter Maximum: "))
mini = 10
maxi = 100

result = MinMaxPalindrome(mini, maxi)
print("Output: ", result)

print("------------------------------------")

# Check if the number is prime or not

from math import sqrt

def isPrime(N):
    for i in range(2, int(sqrt(N))):
        if N % i == 0:
            return False
    return True


num = int(input("Enter the number: "))
print("The",num,"number is Prime or not: ",isPrime(num))

print("------------------------------------")

def is_Prime(N):
    for i in range(2, int(sqrt(N))):
        if N % i == 0:
            return False
    return True

def minMaxPrime(Min, Max):
    Prime_Numbers = []

    for i in range(Min, Max + 1):
        if is_Prime(i):
            Prime_Numbers.append(i)
    return Prime_Numbers

mini = 10
maxi = 50

res = minMaxPrime(mini, maxi)
print("Prime number in range: ",res)

print("------------------------------------")

def Armstrong(n):
    original_no = n
    count = 0
    temp = n

    while temp != 0:
        count += 1
        temp //= 10

    superPower = 0
    while n != 0:
        digit  = n % 10
        superPower += pow(digit, count)
        n //= 10
    return superPower == original_no

n1 = 153
if Armstrong(n1):
    print("Yes, it is a armstrong number.")
else:
    print("No, it is not a armstrong number.")

print("------------------------------------")

a1 = 13
if a1 % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")

print("------------------------------------")

a2 = -6
if a2 >= 0:
    print("Positive.")
else:
    print("Negative.")

print("------------------------------------")

N = 5
sum1 = 0
for i in range(N+1):
    sum1 += i
print(sum1)

print("------------------------------------")

def binary_to_decimal(binary):
    decimal1 = 0
    power = 0
    while binary > 0:
        digit = binary % 10

        decimal1 = decimal1 + digit * (2 ** power)

        binary //= 10

        power += 1
    return decimal1

binary_number = 1011
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)

print("------------------------------------")

def binary_to_octal(binary):
    octal = 0
    decimal = 0
    power = 0

    # Convert binary to decimal
    while binary > 0:
        digit = binary % 10
        decimal += digit * (2 ** power)
        binary //= 10
        power += 1

    # Convert decimal to octal
    power = 0
    while decimal > 0:
        digit = decimal % 8
        octal += digit * (10 ** power)
        decimal //= 8
        power += 1

    return octal

# Example usage
binary_number = 1100110
octal_number = binary_to_octal(binary_number)
print(octal_number)

print("------------------------------------")

def decimal_to_binary(Decimal):
    binary = 0
    power = 0
    while Decimal > 0:
        digit = Decimal % 2
        binary += digit * (10 ** power)
        Decimal //= 2
        power += 1
    return binary

decimal = 15
binary_num = decimal_to_binary(decimal)
print(binary_num)

print("------------------------------------")

def All_number_product(Numm):
    lst = [int(d) for d in str(Numm)]
    prod = 1
    for i in lst:
        prod = prod * i
    return int(prod)

Numm = 5244
product = All_number_product(Numm)
print(product)