class Solution(object):
    def longestValidParentheses(self, s):

        left = right = 0
        max_len = 0

        # left to right
        for ch in s:

            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)

            elif right > left:
                left = right = 0

        left = right = 0

        # right to left
        for ch in reversed(s):

            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)

            elif left > right:
                left = right = 0

        return max_len