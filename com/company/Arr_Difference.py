def Arr_Diff(arr):
    # Convert each element to the most minimized possible form
    minimized_arr = []

    for num in arr:
        while num % 2 == 0:
            num //= 2
        minimized_arr.append(num)

    # After minimizing all elements, calculate the min and max of the array
    min_element = min(minimized_arr)
    max_element = max(minimized_arr)

    # Return the difference between the max and min element
    return max_element - min_element


# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = Arr_Diff(arr)
    print(result)
