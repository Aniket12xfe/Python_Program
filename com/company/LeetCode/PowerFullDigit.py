def powerfulDigit(st, fi, lim, str1):
    count = 0
    for num in range(start, finish+1):
        num_str = str(num)
        if num_str.endswith(s):
            if all(int(d) <= lim for d in num_str):
                count += 1
    return count


# start = 1
# finish = 6000
# limit = 4
# s = "124"
start = int(input())
finish = int(input())
limit = int(input())
s = str(input())
print(powerfulDigit(start, finish, limit, s))