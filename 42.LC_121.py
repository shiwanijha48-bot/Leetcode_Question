class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        n = len(prices)
        for i in range(0, n):
            if min_price > prices[i]:
                min_price = prices[i]
            profit = prices[i] - min_price
            if max_profit < profit:
                max_profit = profit
        return max_profit
