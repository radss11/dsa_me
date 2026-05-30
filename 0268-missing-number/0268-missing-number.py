class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2   # sum of numbers from 0 to n
        actual_sum = sum(nums)
        return expected_sum - actual_sum
