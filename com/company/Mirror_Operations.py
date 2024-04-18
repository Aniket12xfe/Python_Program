input_string = input("Enter the String: ")
n = int(input("Enter n: "))

# creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reverse_alphabets))

# finding the part of the string on which we will do mirror operations
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding mirror operations
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

# printing final result
result = prefix+mirror
print(result)


