class Solution(object):
    def isPalindrome(self, s):

        new = ""

        for ch in s:

            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                new += ch.lower()

        return new == new[::-1]