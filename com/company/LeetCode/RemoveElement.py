# com/company/LeetCode/RemoveElement.py
def removeElement(arr, val):
    return [i for i in arr if i != val]


arr = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(arr, val))
