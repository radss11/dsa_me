class Solution(object):
    def coinChange(self, coins, amount):

        dp = [-1] * (amount + 1)

        def solve(amount):

            if amount == 0:
                return 0

            if amount < 0:
                return float("inf")

            if dp[amount] != -1:
                return dp[amount]

            ans = float("inf")

            for coin in coins:
                ans = min(ans, 1 + solve(amount - coin))

            dp[amount] = ans
            return dp[amount]

        answer = solve(amount)

        if answer == float("inf"):
            return -1

        return answer