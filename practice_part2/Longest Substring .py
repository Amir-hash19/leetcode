def longest_substring(x: str) -> int:
    if not x:
        return 0

    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(x)):
        while x[right] in char_set:
            char_set.remove(x[left])
            left += 1

        char_set.add(x[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# print(longest_substring("absabsbsasbgfhtkopotkgho"))


def longest_substring(x: str) -> str:
    if not x:
        return ""

    char_set = set()
    left = 0
    max_len = 0
    longest = ""

    for right in range(len(x)):
        while x[right] in char_set:
            char_set.remove(x[left])
            left += 1

        char_set.add(x[right])

        
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            longest = x[left:right + 1]

    return longest


print(longest_substring("absabsbsasbgfhtkopotkgho"))
