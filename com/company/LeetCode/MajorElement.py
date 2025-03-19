from collections import Counter

def majorElement(arr):
    count = Counter(arr)
    for i in arr:
        if count[i] > len(arr) // 2:
            return i

# arr = [3, 2, 3]
arr = [2,2,1,1,1,2,2]
print(majorElement(arr))