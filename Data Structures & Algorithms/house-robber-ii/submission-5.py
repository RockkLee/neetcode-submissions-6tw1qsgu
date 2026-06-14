from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def wrp_topdown(i: int, is_1st: bool):
            @lru_cache
            def topdown(i: int) -> int:
                if i == n - 1 and is_1st:
                    return 0
                if i >= n:
                    return 0
                return max(topdown(i + 1), nums[i] + topdown(i + 2))
            return topdown(i)

        return max(wrp_topdown(0, True), wrp_topdown(1, False))
