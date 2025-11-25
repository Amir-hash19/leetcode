class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        s = ''.join(c.lower() for c in s if c.isalnum())

        return s == s[::-1]
        # return s == "".join(reversed(s))
    



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))


