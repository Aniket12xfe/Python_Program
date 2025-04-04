def isPalindrome(s):
    str = "".join(char for char in s if char.isalnum()).lower()
    return str == str[::-1]


str = "A man, a plan, a canal: Panama"
print("".join(str.replace(" ", "").replace(",", "").replace(":", "")).lower())
print(isPalindrome(str))