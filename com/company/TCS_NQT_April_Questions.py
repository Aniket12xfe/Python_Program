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