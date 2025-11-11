def longest_Common_Prefix(s):
    if not s:
        return ""
    
    s.sort()
    first, last = s[0], s[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

s = ["amir", "amirali", "amirmohamad"]

print(longest_Common_Prefix(s))    


    
