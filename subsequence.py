class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            first_number = nums[i]
            for j in range(len(nums)):
                other_numbers = nums[j]
                if i != j and first_number + other_numbers == target:
                    return [i,j]
  
