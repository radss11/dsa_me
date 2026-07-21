class Solution(object):
    def canJump(self, nums):
        maxIndexReached = 0
        for i in range(len(nums)):
            if i>maxIndexReached:
                return False
            else:
                maxIndexReached = max( maxIndexReached, i+nums[i])
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        