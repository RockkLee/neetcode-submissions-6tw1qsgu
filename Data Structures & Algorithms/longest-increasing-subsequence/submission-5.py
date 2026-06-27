from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(prev_i: int, i: int) -> int:
            if i == n:
                return 0

            # Option 1: skip nums[i]
            skip = dfs(prev_i, i + 1)

            # Option 2: take nums[i], if valid
            take = 0
            if prev_i == -1 or nums[i] > nums[prev_i]:
                take = 1 + dfs(i, i + 1)

            return max(skip, take)

        return dfs(-1, 0)