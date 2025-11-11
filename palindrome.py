class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]


test = Solution()

print(test.isPalindrome(111100))





# تعریف نود لیست لینک‌شده
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)  # نود کمکی
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # هرچی باقی مونده رو وصل می‌کنیم
        current.next = list1 if list1 else list2
        
        return dummy.next





class Solution(object):
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
