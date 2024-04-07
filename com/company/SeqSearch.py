def seqSearch(arr, key, n):
    Element = [0] * 10
    index = [0] * 10
    flag = 0
    ind = 0
    start = end = 0
    for i in range(0,n,2):
        Element[ind] = arr[i]
        index[ind] = i
        ind += 1

    if(key < Element[0]):
        print("Element not present")
        exit(0)
    
    else:
        for i in range(1, ind + 1):
            if(key < Element[i]):
                start = index[i - 1]
                end = index[i]
                break
        
    for i in range(start, end + 1):
        if(key == arr[i]):
            flag = 1
            break

    if flag == 1:
        print("Index", i)
    else:
        print("Element is not present")

print("Sequential Search")
arr = [11,15,22,24,26,32,34,38]
n = len(arr)
key = 32
seqSearch(arr, key, n)