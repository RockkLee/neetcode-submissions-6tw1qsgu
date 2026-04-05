from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def topdown_range(l: int, r: int):
            @lru_cache
            def topdown(idx):
                if idx > r:
                    return 0
                return max(nums[idx] + topdown(idx + 2), topdown(idx + 1))

            return topdown(l)
        return max(topdown_range(0, len(nums) - 2), topdown_range(1, len(nums) - 1))
