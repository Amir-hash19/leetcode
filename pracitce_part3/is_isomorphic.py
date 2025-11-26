class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s, mapping_t = {}, {}

        for a, b in zip(s, t):
            if mapping_s.get(a,b) != b or mapping_t.get(b,a) != a:
                return False
            mapping_s[a] = b
            mapping_t[b] = a    



        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))  # True
print(s.isIsomorphic("foo", "bar"))