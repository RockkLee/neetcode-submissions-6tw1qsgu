from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def topdown(i: int) -> int:
            if i > n:
                return 1
            return topdown(i + 1) + topdown(i + 2)
        return topdown(2)