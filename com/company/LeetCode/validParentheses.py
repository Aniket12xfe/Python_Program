def validParentheses(str1):
    stack = []
    for char in str1:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return True


para = "(a+b)*(a-b))"
print(validParentheses(para))