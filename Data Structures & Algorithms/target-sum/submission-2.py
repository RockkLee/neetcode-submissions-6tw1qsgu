from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def topdown(i: int, amt: int) -> int:
            if i == len(nums):
                if target == amt:
                    return 1
                return 0
            return topdown(i + 1, amt + nums[i]) + topdown(i + 1, amt - nums[i])

        return topdown(0, 0)
