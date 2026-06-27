from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i: int, prev_i: int) -> int:
            if i == n:
                return 0

            # Option 1: skip nums[i]
            skip = dfs(i + 1, prev_i)

            # Option 2: take nums[i], if valid
            take = 0
            if prev_i == -1 or nums[i] > nums[prev_i]:
                take = 1 + dfs(i + 1, i)

            return max(skip, take)

        return dfs(0, -1)