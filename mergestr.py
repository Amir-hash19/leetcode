def merge_alternate(word1, word2):
    merged = []
    length = max(len(word1), len(word2))

    for i in range(length):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
    
    return ''.join(merged)

word1 = input()
word2 = input()
result = merge_alternate(word1, word2)
print(result)  

