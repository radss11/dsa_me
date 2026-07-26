class Solution(object):
    def minCut(self, s):

        n = len(s)

        # pal[i][j] = True if s[i...j] is palindrome
        pal = [[False] * n for _ in range(n)]

        # Every single character is palindrome
        for i in range(n):
            pal[i][i] = True

        # Length = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                pal[i][i + 1] = True

        # Length >= 3
        for length in range(3, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j] and pal[i + 1][j - 1]:
                    pal[i][j] = True

        dp = [0] * n

        for i in range(n):

            if pal[0][i]:
                dp[i] = 0
                continue

            dp[i] = float("inf")

            for j in range(i):

                if pal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]