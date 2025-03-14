# def reverse(s):
#     return s[::-1]


# def is_palindrome(s):
#     return s == s[::-1]


# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)


# print(reverse("Hello"))
# print(is_palindrome("racecar"))
# print(is_anagram("listen", "silent"))

def reverse(str):
    return str[::-1]

def is_palindrome(s):
    return s == s[::-1]

def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(TwoSum([2, 7, 11, 15], 9))
print(reverse("Madam"))
print(is_palindrome("Madam"))