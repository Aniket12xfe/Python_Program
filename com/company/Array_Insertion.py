print("How many elements are there in Array?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("Enter the element: ")
    item = int(input())
    array.append(item)

print("Enter the position where you want to add element: ")
position = int(input())

print("Enter the value to insert")
value = int(input())

array = array[:position]+[value]+array[position:]
print("Resultant array \n")
print(array)

for i in array:
    print("\n")
    print(i)