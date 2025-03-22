def maxProfit(arr):
    l, r = 0, 1
    max_profit = 0
    while r < len(arr):
        if arr[l] < arr[r]:
            max_profit = max(max_profit, arr[r] - arr[l])
        else:
            l = r
        r += 1
    return max_profit


# arr = [7,1,5,3,6,4]
arr = [7,6,4,3,1]
print(maxProfit(arr))
