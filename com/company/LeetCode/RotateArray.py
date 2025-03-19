
def rotateArray(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:]+arr[:-k]

# arr = [-1,-100,3,99]
# k = 2
arr = [1,2,3,4,5,6,7]
k = 3
print(rotateArray(arr, k))