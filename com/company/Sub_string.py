def sub_string(str2):
    s = ""
    count = 0
    for i in str2:
        if i not in s:
            s += i
            count += 1
    return count

# str1 = "abcabcbb"
str1 = "bbbbb"
print(sub_string(str1))