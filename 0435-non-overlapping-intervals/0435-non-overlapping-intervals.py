class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        intervals.sort(key=lambda x: x[1])

        count = 0

        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1

        return count