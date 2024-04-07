def countOddEvenDifference(n, number):
    total = 0

    for i in number:
        if i%2 == 0:
            total = total - 1
        else:
            total = total + 1
    return total

n = int(input())
number = list(map(int, input().split()))
print(countOddEvenDifference(n, number))