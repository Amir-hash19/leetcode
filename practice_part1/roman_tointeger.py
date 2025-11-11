class Solution(object):
    def romanToInt(self, s):
        s = list(str(input()))
        for i in range(len(s)):
            if s[i] == "I":
                s[i] = 1
            elif s[i] == "V":    
                s[i] = 5
            elif s[i] == "X":
                s[i] = 10 
            elif s[i] == "L":    
                s[i] = 50
            elif s[i] == "C": 
                s[i] = 100
            elif s[i] == "D":
                s[i] = 500
            elif s[i] == "M":
                s[i] = 1000
        print(sum(s))         
obj = Solution()
obj.romanToInt("IIV")


