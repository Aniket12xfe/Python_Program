row_num = int(input("Input the number of rows: "))
col_num = int(input("Input the number of columns: "))

arr = [[0 for col in range(col_num)] for row in range(row_num)]

for col in range(col_num):
    for row in range(row_num):
        item = int(input("Enter the number: "))
        arr[row][col] = item

print(arr)