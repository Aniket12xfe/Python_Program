def longest_common_substring(str1, str2):
    maxLength = 0
    long_substr = ""
    for i in range(len(str1)):
        for j in range(i+1, len(str1) + 1):
            substr = str1[i:j]

            if substr in str2:
                if len(substr) > maxLength:
                    maxLength = len(substr)
                    long_substr = substr

    return  long_substr


s1 = 'abcdef'
s2 = 'zabcf'
result = longest_common_substring(s1, s2)
print(result)