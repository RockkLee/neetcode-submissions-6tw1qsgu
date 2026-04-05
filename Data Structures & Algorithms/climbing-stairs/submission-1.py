from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        @lru_cache
        def topbuttom(n: int):
            if n == 0:
                return 1
            if n == 1:
                return 1
            return topbuttom(n - 1) + topbuttom(n - 2)
        return topbuttom(n)