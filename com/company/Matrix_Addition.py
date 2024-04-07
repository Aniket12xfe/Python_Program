def matrix_addition(arr1, arr2):
    result = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    print("Addition of two matrices: ")
    print(result)

row_num1 = int(input("Enter the number of rows for matrix 1: "))
col_num1 = int(input("Enter the number of columns for matrix 1: "))
arr1 = [[0 for col in range(col_num1)] for row in range(row_num1)]

for col in range(col_num1):
    for row in range(row_num1):
        item1 = int(input("Enter the elements for matrix 1: "))
        arr1[row][col] = item1
print(arr1)

row_num2 = int(input("Enter the number of rows for matrix 2: "))
col_num2 = int(input("Enter the number of columns for matrix 2: "))
arr2 = [[0 for col in range(col_num2)] for row in range(row_num2)]

for col in range(col_num2):
    for row in range(row_num2):
        item2 = int(input("Enter the elements for matrix 2: "))
        arr2[row][col] = item2
print(arr2)
matrix_addition(arr1, arr2)