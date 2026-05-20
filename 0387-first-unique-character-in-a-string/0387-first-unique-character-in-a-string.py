class Solution(object):
    def firstUniqChar(self, s):

        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Find first unique character
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1