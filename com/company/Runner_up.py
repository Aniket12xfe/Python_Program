N = int(input())
arr = map(int, input().split())

x = sorted(set(arr))
print(x[-2])
