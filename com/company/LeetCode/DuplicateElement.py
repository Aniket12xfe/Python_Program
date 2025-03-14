def removeDuplicate(arr):
    arr1 = set()
    for i in arr:
        arr1.add(i)
    return list(arr1)
    # return list(set(arr))

arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate(arr))

