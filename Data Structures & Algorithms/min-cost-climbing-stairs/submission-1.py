from functools import lru_cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @lru_cache
        def topdown(i: int) -> int:
            if i >= n:
                return 0
            return min(cost[i] + topdown(i + 1), cost[i] + topdown(i + 2))

        return min(topdown(0), topdown(1))
