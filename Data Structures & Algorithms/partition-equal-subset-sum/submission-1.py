from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 > 0:
            return False
        target = summ / 2

        @lru_cache(maxsize=None)
        def backtracking(idx: int, cur_sum: int) -> bool:
            # base case
            if idx == len(nums):
                return False
            if cur_sum == target:
                return True
            # not take it
            if backtracking(idx + 1, cur_sum):
                return True
            # take it
            if backtracking(idx + 1, cur_sum + nums[idx]):
                return True
            return False

        return backtracking(0, 0)
