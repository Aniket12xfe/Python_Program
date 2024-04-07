def findFrequency(lst):
    freq = {}           #take list as input and return key value in dictionary
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq



num = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 5]
print("Frequency of each elements: ",findFrequency(num))