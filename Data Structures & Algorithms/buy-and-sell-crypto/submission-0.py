# 2, 10, 1, 5, 3, 6, 4
# 
# min_price, max_profit
# 0: 2,0 -> 1: 2,8 -> 2: 1,10 -> 3: 1,10 ...
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100
        max_profit = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit
