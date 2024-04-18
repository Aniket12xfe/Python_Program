import textwrap

def wrap_string(string1, wrap):
    # string1 = textwrap.fill(string1, wrap)
    result = ""
    for i in range(0, len(string1), w):
        result += string1[i:i+wrap] + "\n"
    return result

s = input("Enter a string: ")
w = int(input("Enter the width: "))

# Wrap the string into a paragraph of width w
wrapped_string = wrap_string(s, w)
print("Wrapped string:")
print(wrapped_string)