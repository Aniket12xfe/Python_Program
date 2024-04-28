# find the largest number using given number 542789

num = int(input("Enter the number: "))

lst = [int(d) for d in str(num)]

lst.sort(reverse=True)

print(int("".join(map(str,lst))))

print("--------------------------------------")

# we have input value 12 assume,
# and vendor has weights 1,2,5,10,20,50,100,500,1000 we have print count of weights assign to input like a list present 2,
# 10 and there sum is 12 which is match with input value, so we require 2 as count of weights

def count_weight(Input_value, w):
    w.sort(reverse=True)
    Count = 0
    Weight_Count = [0] * len(w)

    for i, weight in enumerate(w):
        Count += Input_value // weight
        Weight_Count[i] = Input_value // weight
        Input_value %= weight
    return Count, Weight_Count

W = [1,2,5,10,20,50,100,500,1000]
input_value = int(input("Enter the Input: "))
count, weight_count =count_weight(input_value, W)
print("Minimum number of weights required:", count)
print("Weight count:", weight_count)

print("--------------------------------------")

# unique path with obstacles matrix problem

def unique_paths_with_obstacles(Obstacle_grid, row, col):
    # Base case: If the current cell is an obstacle or out of bounds, return 0
    if row >= len(Obstacle_grid) or col >= len(Obstacle_grid[0]) or Obstacle_grid[row][col] == 1:
        return 0

    # Base case: If we reached the bottom-right corner, return 1
    if row == len(Obstacle_grid) - 1 and col == len(Obstacle_grid[0]) - 1:
        return 1

    # Recursive case: Move right and down and sum the results
    return unique_paths_with_obstacles(Obstacle_grid, row, col + 1) + unique_paths_with_obstacles(Obstacle_grid, row + 1, col)


# Example usage
obstacle_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

print(unique_paths_with_obstacles(obstacle_grid, 0, 0))  # Output: 2

print("--------------------------------------")

# To find the subarray and compare with the target array a = [3,4,-1,4] find the subarray which concludes the target = 7 print 4

def find_sub_array(a, t):
    start = 0
    end = 0
    current_sum = 0

    while end < len(a):
        current_sum = current_sum + a[end]

        while start <= end and current_sum > target:
            current_sum = current_sum - a[start]
            start = start + 1

        if current_sum == target:
            return a[start: end + 1]
        end = end + 1

    return None


a = [3,4,-1,4]
target = 7
print(find_sub_array(a, target))

