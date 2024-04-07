def swap_number(list, idx1, idx2):
    # Swapping values at idx1 and idx2
    temp = list[idx1]
    list[idx1] = list[idx2]
    list[idx2] = temp
    return list



n = int(input("Enter the size of list: "))
list = []

for _ in range(n):
    num = int(input(""))
    list.append(num)

idx1 = int(input("Enter the index1: "))
idx2 = int(input("Enter the index2: "))

print("Before swapping ",list)
result = swap_number(list, idx1, idx2)
print("After swapping ",result)
