n = int(input())
lst = []

for i in range(n):
    item = int(input())
    lst.append(item)
print(lst)

result = 0
for j in range(1, n+1):
    # result = sum(lst)       #inbuild function
    result += j         #logical function
print(result)

print('---------------------------------------------------')
def helloWorld():
    print("Hello World!!")

helloWorld()

print("----------------------------------------------------")
def sum_function(n1, n2):
    print(n1+n2)

sum_function(2, 3)