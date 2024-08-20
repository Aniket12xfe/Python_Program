def lengthOfLongestSubstring(str1):
    new = ""
    count = 0
    for i in str1:
        if i not in new:
            new += i
            count += 1
    return count


str1 = input()
print(lengthOfLongestSubstring(str1))