def Solve(inputx):
    listy = []
    count = 1
    for i in range(1, len(inputx)):
        if inputx[i] == inputx[i-1]:
            count += 1
        else:
            if count > 1:
                listy.append(f'{count}{inputx[i-1]}')
            else:
                listy.append(inputx[i-1])
            count = 1

    if count > 1:
        listy.append(f'{count}{inputx[-1]}')
    else:
        listy.append(inputx[-1])

    return ''.join(listy)


inputs = "aaabccde"
print(Solve(inputs))