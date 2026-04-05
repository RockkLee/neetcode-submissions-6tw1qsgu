from functools import lru_cache
from typing import List, Tuple


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @lru_cache(None)
        def topdown(amt: int) -> int:
            if amt > amount:
                return -1
            if amt == amount:
                return 0
            min_cnt = float('inf')
            for coin in coins:
                cnt = topdown(amt + coin)
                if cnt != -1:
                    min_cnt = min(min_cnt, 1 + cnt)
            return min_cnt if min_cnt != float('inf') else -1

        return topdown(0)