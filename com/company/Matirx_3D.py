row_num3 = int(input("Enter the row numbers: "))
col_num3 = int(input("Enter the col numbers: "))
dim_num = int(input("Enter the dimension numbers: "))

array = [] #creating an empty arr

for dim in range(dim_num):
    array.append([])
    for row in range(row_num3):
        array[dim].append([])
        for col in range(col_num3):
            item = int(input("Enter the numbers: "))
            array[dim][row].append(item)

print("Print 3D Array: ")
for dim in range(dim_num):
    for row in range(row_num3):
        for col in range(col_num3):
            print(array[dim][row][col], end=' ')
        print()
    print("----------------")