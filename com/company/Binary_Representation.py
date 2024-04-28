import math

def decimal_to_binary(Decimal):
    binary = 0
    power = 0
    while Decimal > 0:
        digit = Decimal % 2
        binary += digit * (10 ** power)
        Decimal //= 2
        power += 1
    return binary

def Toggle_bits(decimal):
    k = (1 << int(math.log2(decimal))+ 1) - 1
    return decimal ^ k

decimal = int(input())
binary_num = decimal_to_binary(decimal)
toggle = Toggle_bits(decimal)
print(toggle)
print(binary_num)