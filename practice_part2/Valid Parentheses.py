def is_valid(s):
    pairs = {')': '(', '}': '{', ']': '['}

    stack = []
    """ soled with stack idea !"""
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


print(is_valid("({)}"))