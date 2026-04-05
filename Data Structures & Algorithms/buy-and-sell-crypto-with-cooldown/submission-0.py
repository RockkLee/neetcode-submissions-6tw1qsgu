from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        REST = "REST"
        HOLD = "HOLD"
        CD = "CD"

        @lru_cache(maxsize=None)
        def backtracking(idx: int, state: str) -> int:
            if idx == len(prices):
                return 0
            if state == REST:
                return max(
                    backtracking(idx + 1, REST),  # Do nothing
                    backtracking(idx + 1, HOLD) - prices[idx]  # Buy
                )
            if state == HOLD:
                return max(
                    backtracking(idx + 1, HOLD),  # Do nothing
                    backtracking(idx + 1, CD) + prices[idx]  # Sell
                )
            # if state == CD
            return backtracking(idx + 1, REST)

        return backtracking(0, REST)