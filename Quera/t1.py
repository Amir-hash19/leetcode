import re

def slugify(s) -> str:
    if not isinstance(s, str):
        return "input must be string"

  
    lowered_s = s.lower()


    words = lowered_s.split()


    i = 0
    while i < len(words) - 1:
        if words[i] == "iran" and words[i + 1] == "server":
            words[i] = "iranserver"
            del words[i + 1]
        else:
            i += 1


    result = " ".join(words)


    cleaned = re.sub(r"[^a-z]", "-", result)

    return cleaned


print(slugify("welcome to iran server"))


