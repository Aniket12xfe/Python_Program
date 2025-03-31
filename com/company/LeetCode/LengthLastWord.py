def lastWordLen(s):
    arr = s.split()
    # print(arr)
    return len(arr[-1])


s = "Hello World"
print(lastWordLen(s))