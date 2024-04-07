def search(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

n = int(input())
array = []
i = 0
for i in range(n):
    print("Enter elements: ")
    item = int(input())
    array.append(item)

print("Enter the key: ")

k = int(input())

loc = search(array, k)
print("Index of element is: ",loc)