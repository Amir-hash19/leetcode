def palindrome_int(x):
    if not x:
        return None
    """this question solved by reveresing an intger with strings mthode"""
    string_number = str(x)
    reversed_number = "".join(reversed(string_number))
    if string_number == reversed_number:
        return True
    return False


print(palindrome_int(999))