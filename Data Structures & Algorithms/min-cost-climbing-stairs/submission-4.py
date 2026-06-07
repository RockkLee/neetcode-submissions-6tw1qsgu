from functools import lru_cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # @lru_cache
        # def topdown(i: int) -> int:
        #     if i >= n:
        #         return 0
        #     return min(cost[i] + topdown(i + 1), cost[i] + topdown(i + 2))
        # return min(topdown(0), topdown(1))
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        bottomup = [0] * n
        bottomup[0] = cost[0]
        bottomup[1] = cost[1]
        for idx in range(2, n): 
            bottomup[idx] = cost[idx] + min(bottomup[idx - 1], bottomup[idx - 2])
        return min(bottomup[len(cost) - 1], bottomup[len(cost) - 2])
