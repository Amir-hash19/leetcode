class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointers for nums1, nums2, and the merged array
        i = m - 1  # last element in the valid part of nums1
        j = n - 1  # last element in nums2
        k = m + n - 1  # last position in nums1

        # Merge nums1 and nums2 starting from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are any remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Example of how to use the class
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # Create an instance of Solution and call the merge function
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)  # Output should be [1, 2, 2, 3, 5, 6]
