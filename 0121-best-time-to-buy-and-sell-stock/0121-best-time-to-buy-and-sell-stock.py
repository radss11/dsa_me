class Solution(object):
    def maxProfit(self, prices):

        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):

            if prices[i] < minPrice:
                minPrice = prices[i]

            profit = prices[i] - minPrice

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit