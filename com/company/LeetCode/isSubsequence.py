def isSubsequence(s, t):
    # i = j = 0
    # while i < len(s) and j < len(t):
    #     if s[i] == t[j]:
    #         i += 1
    #     j += 1
    # return i == len(s)
    t_iter = iter(t)
    return all(c in t_iter for c in s)

s = "abc"
t = "ahbgdc"
# s= "axc"
# t = "ahbgdc"
print(isSubsequence(s, t))