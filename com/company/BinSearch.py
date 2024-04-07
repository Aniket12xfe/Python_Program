def BinSearch(arr, k):
    low = 0
    high = len(arr)-1
    m = 0
    while(low <= high):
        m = (low+high)//2
        if(k<arr[m]):
            high = m - 1
        elif(k>arr[m]):
            low = m + 1
        else:
            return m
    return -1

n = int(input())
array = []
i = 0

for i in range(n):
    print("Enter the elements: ")
    item = int(input())
    array.append(item)

print("Enter the key: ")
k = int(input())

loc = BinSearch(array, k)
if(loc != -1):
    print("The element is present at index: ", loc)
else:
    print("Element not present..")