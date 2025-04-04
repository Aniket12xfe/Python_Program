def TwoSum(nums, target):
    # Two pointers Approach

    # left = 0
    # right = len(nums)-1
    # while left < right:
    #     total = nums[left] + nums[right]
    #     if total == target:
    #         return [left+1, right+1]
    #     elif total > target:
    #         right -= 1
    #     else:
    #         left += 1

    # Hashmap Approach
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff]+1, i+1]
        seen[num] = i
    return []
    
arr = [2, 7, 11, 15]
target = 9
print(TwoSum(arr, target))