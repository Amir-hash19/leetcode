class Solution:
    def canConstruct(self, ransomNote: str, magazine: str)->bool:
        if not ransomNote and not magazine:
            return False
        
        chars_ransomNote = list(ransomNote)
        chars_magazine = list(magazine)

        for ch in chars_ransomNote:
            if ch in chars_magazine:
                chars_magazine.remove(ch)
            else:
                return False
        return True        


s = Solution()
print(s.canConstruct(ransomNote="a",magazine="abca"))




        

        