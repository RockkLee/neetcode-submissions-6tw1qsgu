class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        # @lru_cache
        # def topbottom(n: int):
        #     if n == 0:
        #         return 1
        #     if n == 1:
        #         return 1
        #     return topbottom(n - 1) + topbottom(n - 2)
        # return topbottom(n)
        bottomup = [0] * (n + 1)
        bottomup[0], bottomup[1] = 1, 1
        for i in range(2, n + 1):
            bottomup[i] = bottomup[i - 1] + bottomup[i - 2]
        return bottomup[n]
