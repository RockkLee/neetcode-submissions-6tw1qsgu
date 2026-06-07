from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        # @lru_cache
        # def topdown(i: int) -> int:
        #     if i >= n:
        #         if i == n:
        #             return 1
        #         return 0
        #     return topdown(i + 1) + topdown(i + 2)
        # 
        # return topdown(0)
        
        # buttom up
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [-1] * (n)
        dp[0] = 1
        dp[1] = 2
        for idx in range (2, n):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
        return dp[n - 1]