def jumpGame(arr):
    goal = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] + i >= goal:
            goal = i
    return True if goal == 0 else False

arr = [2,3,1,1,4]
# arr = [3,2,1,0,4]
print(jumpGame(arr))