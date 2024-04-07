def RecBinSearch(arr, k, low, high):
    if(high>=low):
        m = (low+high)//2
        if(arr[m]==k):
            return m
        elif(arr[m]>k):
            return RecBinSearch(arr,k,low,m-1)
        else:
            return RecBinSearch(arr,k,m+1,high)
    else:
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

loc = RecBinSearch(array,k,0,len(array)-1)
if(loc != -1):
    print("The element is present at index: ", loc)
else:
    print("Element not present..")
        