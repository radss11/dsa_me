class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            # Remove the lowest set bit
            n &= (n - 1)
            count += 1
        return count
