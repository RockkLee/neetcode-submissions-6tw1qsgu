from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def topdown(amt: int):
            if amt == 0:
                return 0
            res = 1e91
            for coin in coins:
                nxt_amt = amt - coin
                if nxt_amt >= 0:
                    res = min(res, 1 + topdown(nxt_amt))
            return res
        
        minCoins = topdown(amount)
        return -1 if minCoins >= 1e9 else int(minCoins)