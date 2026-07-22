class Solution(object):
    def rob(self, nums):

        dp = [-1] * len(nums)

        def solve(i):

            if i >= len(nums):
                return 0

            if dp[i] != -1:
                return dp[i]

            rob = nums[i] + solve(i+2)

            skip = solve(i+1)

            dp[i] = max(rob, skip)

            return dp[i]

        return solve(0)