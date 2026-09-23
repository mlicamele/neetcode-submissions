class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        oldP = prices[0]

        for p in prices:
            profit = max(profit, p - oldP)
            oldP = min(oldP, p)
        return profit
            
                