class Solution(object):

    def longestPalindrome(self, s):

        start = 0
        max_len = 0

        for i in range(len(s)):

            # check odd and even length palindromes
            for l, r in [(i, i), (i, i + 1)]:

                while l >= 0 and r < len(s) and s[l] == s[r]:

                    l -= 1
                    r += 1

                # current palindrome length
                curr_len = r - l - 1

                if curr_len > max_len:

                    start = l + 1
                    max_len = curr_len

        return s[start:start + max_len]