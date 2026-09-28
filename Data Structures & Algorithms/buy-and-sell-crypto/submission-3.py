class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        profit = 0
        l, r = 0, 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            profit = max(profit, curr_profit)

            if curr_profit < 0:
                l += 1
            else:
                r += 1

        return profit