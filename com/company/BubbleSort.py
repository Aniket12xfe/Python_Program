def sort(nums):
    for i in range(x-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

def selectionSort(nums):
    for i in range(x-1):
        minx = i
        for j in range(i, x):
            if nums[j] < nums[minx]:
                minx = j
        temp = nums[i]
        nums[i] = nums[minx]
        nums[minx] = temp

        print(nums)


lists = [5, 3, 8, 6, 7, 2]
x = len(lists)
# for i in range(0, x-1):
#     for j in range(i):
#         if lists[j] < lists[i]:
#             temp = lists[j]
#             lists[j] = lists[i]
#             lists[i] = temp
# sort(lists)
selectionSort(lists)
print("The sorted list is as follows: ", lists)