# smallest element in array

ele = [2,5,1,3,0]
ele.sort()
print(ele[0])

print("---------------------------")

# largest element in array

lar = [2,5,1,3,0]
ele.sort()
print(ele[-1])

print("---------------------------")

# second largest and second largest element

sec = [2,5,1,3,0]
sec.sort()
print("Second largest: ", sec[-2], " Second smallest: ", sec[1])

print("---------------------------")

# Reverse a given array

rev = [2,5,1,3,0]
# result = reversed(sec)
result = rev[::-1]
print(result)

print("---------------------------")

# Count the frequency of each element in an array
arr = [10,5,10,15,10,5]
freq = {}
for item in arr:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)

# if we don't use dict in a problem then
n = len(arr)
visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    count = 1
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            visited[j] = True
            count += 1
    print(arr[i], count)

print("---------------------------")

# Rearrange array in first half in ascending order and another half is in descending

arr = [8,7,1,6,5,9]
n = len(arr)
half = n // 2
arr[:half]=sorted(arr[:half])
arr[half:]=sorted(arr[half:], reverse=True)
a1 = arr[:half] + arr[half:]
print(a1)         # My logic, which is now corrected

# n = len(arr)
# mid = n // 2
# arr[:mid] = sorted(arr[:mid])
# arr[mid:] = sorted(arr[mid:], reverse=True)
# print(arr)

# print("---------------------------")

# sum of elements in array
# n = int(input("Enter the size: "))
# s = []
# for i in range(n):
#     item = int(input())
#     s.append(item)
# print(s)
#
# sum_arr = 0
# for i in range(n):
#     sum_arr += s[i]
# print("The sum of elements in array: ",sum_arr)

print("---------------------------")

# Rotate array by K elements: Block Swap Algorithm

def rotate_array(arr1, k):
    n1 = len(arr1)
    k = k % n1  # Normalize k if it's larger than n

    # # Reverse the first part
    arr1[k:] = reversed(arr1[k:])
    # # Reverse the second part
    arr1[:k] = reversed(arr1[:k])
    # # Reverse the whole array
    arr1.reverse()

# Input array and K values
arr = [1, 2, 3, 4, 5]
K = 2

# Rotate the array by K elements
rotate_array(arr, K)

# Print the rotated array
print(arr)

print("---------------------------")

# Average of elements in arrays
def Avg_arr(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)
arr1 = [161, 182 ,161 ,154 ,176, 170 ,167 ,171, 170, 174]
print("Average of array: ",Avg_arr(arr1))
# n2 = len(arr1)
# Avg = 0
# sum_arr = 0
#
# for i in range(n2):
#     sum_arr = sum(arr1)
#     Avg = float(sum_arr / n2)
# print(Avg)

print("---------------------------")

# Median of Array
def median_of_array(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        # For even-length array, return the average of the middle two elements
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        # For odd-length array, return the middle element
        return arr[n // 2]

# Example array
arr = [2,5,1,7]
print("Median:", median_of_array(arr))  # Output: 3 (median of 1, 3, 2, 4, 5 is 3)

print("---------------------------")

# using import statistics

import statistics

median = statistics.median(arr)
print(median)

print("---------------------------")

# Removing duplicates from array
dup = [1,1,1,2,2,2,3,3,3]
# dup = [2,3,1,9,3,1,3,9]
m = set()

for i in dup:
    if i not in m:
        m.add(i)
print(list(m))

print("---------------------------")

# Removing duplicates from an unsorted array

def un_sorted_dup(num):
    seen_dup = set()
    duplicate = []
    for element in num:
        if element not in seen_dup:
            duplicate.append(element)
            seen_dup.add(element)

    return duplicate

un_arr = [4,3,9,2,4,1,10,89,34]
print(un_sorted_dup(un_arr))

print("---------------------------")

# Adding elements in array
Add = [1,2,3,4,5]
Add.insert(0, 6)
Add.insert(-1, 7)
Add.insert(4, 8)
print(Add)

print("---------------------------")

# Find a repeating element in an array

rep_arr = [1,1,0]
seen = set()
repeating = set()

for i in rep_arr:
    if i in seen:
        repeating.add(i)
    else:
        seen.add(i)
print(list(repeating))

print("---------------------------")

# Find a non-repeating element in an array
non_rep_arr = [1,2,-1,1,3,1]
non_repeating = {}

for i in non_rep_arr:
    if i in non_repeating:
        non_repeating[i] += 1
    else:
        non_repeating[i] = 1
non_repeating_elements = [num for num, count in non_repeating.items() if count == 1]
print(non_repeating_elements)

print("---------------------------")

# Average function using sets most optimum solution

def average(array):
    return float(sum(set(array)) / len(set(array)))

# arr = [161, 182 ,161 ,154 ,176, 170 ,167 ,171, 170, 174]
arr = [1,2,3,4,5]
print("Average using set function: ",average(arr))

print("---------------------------")

# cartesian product
A = [1,2]
B = [3,4]

from itertools import product
for i in sorted(tuple(product(A,B))):
    print(i, end="")
print()

print("---------------------------")

# Symmetric Pairs in array

def find_symmetric_pairs(Pair):
    Seen = {}
    symmetric_pair = []

    for Pair in Pair:
        first, second = Pair
        if (second, first) in Seen:
            symmetric_pair.append((first, second))
            symmetric_pair.append((second, first))
        else:
            Seen[Pair] = True

    return symmetric_pair

# Input array of pairs
pairs = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]

# Find symmetric pairs
symmetric_pairs = find_symmetric_pairs(pairs)
print("Symmetric Pairs:")
for pair in symmetric_pairs:
    print(pair)

print("---------------------------")

# Maximum product of subarray
def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    results = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        results = max(results, max_product)

    return results

# Example array
nums = [1, 2, -3, 0, -4, -5]
print("Maximum product of subarray:", max_product_subarray(nums))  # Output: 20

print("---------------------------")

# Rank of array elements

# r_arr = [20,15,26,2,98,6]
# new_arr = []
# for i in r_arr:
#     new_arr.append(i)
#     new_arr.sort()
# print(new_arr)
#
# for i in range(len(new_arr)):
#     print(i, end=" ")

# optimum solution for array
# def replace_by_rank(arr):
#     sorted_arr = sorted(arr)
#     rank_map = {val: i+1 for i, val in enumerate(sorted_arr)}
#     return  [rank_map[val] for val in arr]
#
# arr = [10, 8, 15, 12, 6, 20]
# result = replace_by_rank(arr)
# print("Array after replacing by rank:", result)

# rank the array using inbuilt function rank-data

from scipy.stats import rankdata

def rank_data(arr):
    ranks = rankdata(arr, method='dense')
    return ranks

arr = [20,15,26,2,98,6]
result = rank_data(arr)
print("Array after replacing by rank:", result)

print("---------------------------")

# Factorial of number using function

def Factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for fun in range(1, n+1):
            ans *= fun
    return ans


fac = int(input("Enter N: "))
output = Factorial(fac)
print("The factorial of number is: ", output)

print("---------------------------")

# String Palindrome
str8 = input("Enter the string: ")
str8 = (str8.replace(" ", "").lower())
rev = str8[::-1]
if str8 == rev:
    print("String is palindrome.")
else:
    print("String is not palindrome.")

print("---------------------------")

array = [1,2,3,4,5]
k = 3
for i in range(1, len(array)+1):
    if array[i] == k:
        print("The answer is ",i)
        break

print("---------------------------")

# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [2,4,3,1,7,5,15]
# Output: arr1[] is a subset of arr2[]

arr1 = [1,3,4,5,2]
arr2= [2,4,3,1,7,5,15]

arr1 = set(arr1)
arr2 = set(arr2)

if arr1.issubset(arr2):
    print("arr1[] is a subset of arr2[]")
