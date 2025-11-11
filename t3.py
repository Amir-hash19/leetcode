def palindrome(word):
    new_list = list(str(word))
    rev_list = reversed(new_list)
    str_list = "".join(rev_list)
    if str_list == str(word):
        return True
    else:
        return False

print(palindrome("kkk"))


    
