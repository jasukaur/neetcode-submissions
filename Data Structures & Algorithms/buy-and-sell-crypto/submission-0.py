class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = prices[0], prices[0], 0

        for p in prices:
            if p< buy:
                buy = p
                sell = p
            if p > sell:
                sell = p
                profit = max(profit, sell-buy)
            
        return profit



