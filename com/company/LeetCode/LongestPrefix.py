def longestCommonPrefix(strs):
    prefix = ""
    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix


# strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))