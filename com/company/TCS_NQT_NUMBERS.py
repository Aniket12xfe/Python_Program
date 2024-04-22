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

