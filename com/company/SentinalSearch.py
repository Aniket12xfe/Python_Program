def search(arr, x):
    l = len(arr)
    arr.append(x)
    i = 0
    while arr[i] != x:
        i = i + 1
    if i != 1:
        return i
    else:
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
if location != -1:
    print("The index of the element is; ",location)
else:
    print("Not Found...")
