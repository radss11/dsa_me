class Solution(object):
    def findMaxAverage(self, nums, k):

        left = 0
        windowSum = 0
        maxSum = float("-inf")

        for right in range(len(nums)):

            windowSum += nums[right]

            if right - left + 1 == k:

                if windowSum > maxSum:
                    maxSum = windowSum

                windowSum -= nums[left]
                left += 1

        return maxSum / float(k)