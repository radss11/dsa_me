class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        # check all numbers from 0 to n (inclusive)
        for i in range(n + 1):
            if i not in nums:
                return i   