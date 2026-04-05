class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # @lru_cache
        # def topdown(idx: int, sum: int):
        #     if idx == len(cost) - 1 or idx == len(cost) - 2:
        #         return sum
        #     return min(topdown(idx + 1, cost[idx + 1] + sum), topdown(idx + 2, cost[idx + 2] + sum))

        # return topdown(-1, 0)

        bottomup = [0] * len(cost)
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        bottomup[0], bottomup[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            bottomup[i] = min(bottomup[i - 1], bottomup[i - 2]) + cost[i]
        return min(bottomup[len(cost) - 1], bottomup[len(cost) - 2])
