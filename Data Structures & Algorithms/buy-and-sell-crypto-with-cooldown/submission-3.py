from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        REST = 0
        EMPTY = 1
        HOLD = 2
        @cache
        def topdown(i: int, state: int) -> int:
            if i >= len(prices):
                return 0
            if state == REST:
                return topdown(i + 1, EMPTY)
            if state == EMPTY:
                return max(
                    topdown(i + 1, HOLD) - prices[i],
                    topdown(i + 1, EMPTY)
                )
            # if state == HOLD:
            return max(
                topdown(i + 1, REST) + prices[i],
                topdown(i + 1, HOLD)
            )

        return topdown(0, EMPTY)