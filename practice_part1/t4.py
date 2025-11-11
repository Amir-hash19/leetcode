def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  

    for char in s:
        if char in mapping.values(): 
            stack.append(char)
        elif char in mapping.keys(): 
            if not stack or stack.pop() != mapping[char]:
                return "NO"
    
    return True if not stack else False



