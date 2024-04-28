def sort_Array(List):
    for i in sorted(List):
        print(i, end=" ")


n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

sort_Array(lst)
