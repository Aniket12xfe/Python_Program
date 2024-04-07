size, k = map(int, input().split())
arr = map(int, input().split())

result = 0
counter = 0
m = k
flag = False

for i in arr:
    if flag == False:
        if i >= 0:
            counter = counter + 1
            result = result + i
            m = k
        else:
            if counter == 0:
                print(abs(sum(arr)))
                flag = True
            else:
                m = m - 1
                if m<0:
                    result = result + abs(i)
                else:
                    result = result + i
    else:
        break

if flag == False:
    print(abs(result))