def binsearch(arr, KEY):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low+high)//2
        if KEY < arr[mid]:
            high = mid - 1
        elif KEY > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

print("How many element do you want in Array?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("Enter the elements do you want to Add: ")
    item = int(input())
    array.append(item)

print("Resultant Array is: ")
print(array)

print("Enter the element for search: ")
key = int(input())

location = binsearch(array, key)

if location != -1:
    print("Element at index: ",location)
else:
    print("Element not found")

