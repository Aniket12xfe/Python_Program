def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print("How many elements do you want")
n = int(input())
array = []
i = 0
for i in range(n):
    print("Enter the elements do you want in array")
    item = int(input())
    array.append(item)

print("Resultant array is: ")
print(array)

print("Enter the key do you want to search?")
key = int(input())

location = search(array, key)
print("The element present in array at index: ",location)