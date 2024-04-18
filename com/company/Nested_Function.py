def outerFunction():
    x = 1  # outer function can be declared

    def innerFunction():
        y = 2          # inner function can be declared
        result = x + y
        return result

    return innerFunction()

output = outerFunction()
print(output)