print("How many element you want in array?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("Enter the elements: ")
    item = int(input())
    array.append(item)

print("Enter the index form where you want to delete element: ")
position = int(input())
array = array[:position]+array[position+1:]
print("Resultant array is \n")
print(array)