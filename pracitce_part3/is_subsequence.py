class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and t:
            return True
        elif not t and s:
            return False
        elif not t and not s:
            return True

        
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
                if i == len(s):
                    return True
        return False
            



print(Solution().isSubsequence("axc", "ahbgdc"))


    