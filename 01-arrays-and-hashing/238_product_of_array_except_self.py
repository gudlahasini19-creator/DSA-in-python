# LeetCode 238: Product of Array Except Self
# Time Complexity: O(N)
# Space Complexity: O(1) extra space (excluding output array)

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        
        # Pass 1: Prefix products (all elements to the left)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Suffix products (all elements to the right)
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
