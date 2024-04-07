def mergearrays(arr1, arr2, n1, n2, arr3):
    i = 0
    j = 0
    k = 0

    while i < n1:
        arr3[k] = arr1[i]
        k += 1
        i += 1

    while j < n2:
        arr3[k] = arr2[j]
        k += 1
        j += 1

    arr3.sort()

print("How many elements are there in Array1?")
n1 = int(input())
arr1 = []
i = 0
for i in range(n1):
    print("Enter the element: ")
    item = int(input())
    arr1.append(item)

print("How many elements are there in Array2?")
n2 = int(input())
arr2 = []
i = 0
for i in range(n2):
    print("Enter the element: ")
    item = int(input())
    arr2.append(item)

arr3 = [0 for i in range(n1+n2)]
mergearrays(arr1, arr2, n1, n2, arr3)
print("Merging of two arrays: ")
for i in range(n1+n2):
    print(arr3[i], end = " ")