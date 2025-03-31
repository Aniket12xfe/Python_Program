def firstOccurance(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode"
needle = "leeto"
# print(haystack.find(needle))
# print(haystack.index(needle))
print(firstOccurance(haystack, needle))