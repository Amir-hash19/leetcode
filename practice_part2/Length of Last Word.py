def find_last_word_lenght(s):
    if not s:
        return ""
    
    striped_word = s.strip()
    words = striped_word.split()
    last_word = words[-1]
    count = len(last_word)
    return count



print(find_last_word_lenght("   hello world   "))