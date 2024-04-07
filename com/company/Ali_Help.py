N = 9
data = input()
output = []

if data[2] in ['A', 'E', 'I', 'O', 'U', 'Y']:
    print("invalid")
    exit(0)
if N == len(data):
    for i in range(len(data)-1):
        if data[i].isnumeric() and data[i + 1].isnumeric():
            if int(data[i])+int(data[i + 1])%2==0:
                print("valid")
            else:
                print("invalid")
                exit(0)
        else:
            print("invalid")


# Partially Accepted

# s = input()
# vowel = ["A","E","I","O","U","Y"]
#
# if s[2] in vowel:
#     print("invalid")
# elif (int(s[0])+int(s[1])%2==0) and (int(s[3])+int(s[4])%2==0) and (int(s[4])+int(s[5])%2==0) and (int(s[7])+int(s[8])%2==0):
#     print("valid")
# else:
#     print("invalid")
