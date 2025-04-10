def minOperations(arr, k):
    if any(x < k for x in arr):
        return -1

    greater_value = {x for x in arr if x>k}
    # print(type(greater_value))
    return len(greater_value)


arr = [5,2,5,4,5]
k = 2
print(minOperations(arr, k))