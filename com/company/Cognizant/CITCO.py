# Code 1

def ArraySort(arr):
    non_zero = []
    zero = []
    for i in arr:
        if i != 0:
            non_zero.append(i)
        else:
            zero.append(0)
    return non_zero + zero

arr = [2, 4, 0, 8, 0, 0, 6]
print(ArraySort(arr))

# Code 2
def charDict(arr):
    arr1 = ''.join(arr)
    count = {}
    for i in arr1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count 


arr = ['abb', 'bcc', 'bbd']
print(charDict(arr))

