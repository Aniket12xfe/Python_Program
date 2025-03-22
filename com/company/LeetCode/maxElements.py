def maxElements(arr, max, min):
    count = 0
    for i in arr:
        if i >= min and i <= max:
            count += 1
    return count
    

arr = [5, 10, 12, 15, 18, 20, 25, 30]
max = 20
min = 10
print(maxElements(arr, max, min))
