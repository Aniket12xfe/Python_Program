s = input()
a = int(input())
m = {
 "mon": 6, "tue": 5, "wed": 4,
 "thu": 3, "fri": 2, "sat": 1,
 "sun": 0
 }
ans = 0
if a - m[s[:3]] >= 1:
    ans = 1 + (a - m[s[:3]]) // 7
print(ans)
