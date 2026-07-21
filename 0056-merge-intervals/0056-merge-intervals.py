class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        merged = [intervals[0]]

        for i in range (1,len(intervals)):
            if intervals[i][0]<=merged[-1][1]:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
        return merged

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        