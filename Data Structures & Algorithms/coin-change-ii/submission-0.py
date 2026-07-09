from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def topdown(idx: int, summ: int) -> int:
            if idx == len(coins) or summ > amount:
                return 0
            if summ == amount:
                return 1
            total = 0
            for i in range(idx, len(coins)):
                total += topdown(i, summ + coins[i])
            return total

        return topdown(0, 0)

