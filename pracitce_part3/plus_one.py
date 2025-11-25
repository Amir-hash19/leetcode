class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return False
        

        digits[-1] += 1
        new_digits = [int(digit) for num in digits for digit in str(num)]
        return new_digits
    
print(Solution().plusOne([9]))    
    