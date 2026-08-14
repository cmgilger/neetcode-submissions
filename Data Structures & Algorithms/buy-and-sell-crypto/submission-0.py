class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # selling - buying
        max_profit = 0
        for i, buy in enumerate(prices):
            sell = max(prices[i::1]) - buy
            max_profit = max(sell, max_profit)
        return max_profit