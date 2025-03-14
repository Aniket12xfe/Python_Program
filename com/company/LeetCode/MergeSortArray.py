def mergearrays(arr1, arr2, m, n):
    # for i in range(n):
    #     arr1[m+i] = arr2[i]
    # arr1.sort()
    # return arr1
    num1 = []
    for i in arr1:
        if i != 0:
            num1.append(i)
    arr1 = num1 + arr2
    arr1.sort()
    return arr1

arr1 = [0]
m = 0
arr2 = [1]
n = 1
print(mergearrays(arr1, arr2, m, n))



