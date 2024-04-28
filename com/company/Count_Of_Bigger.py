def Bigger_first(arr):
    count = 1
    max_so_far = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_so_far:
            count += 1
            max_so_far = arr[i]

    return count


arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))

big = Bigger_first(arr)
print(big)
