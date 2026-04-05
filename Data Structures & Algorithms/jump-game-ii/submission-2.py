from functools import lru_cache


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def topdown(idx: int) -> int | float:
            if idx >= n - 1:
                return 0
            paths = []
            if nums[idx] == 0:
                return 0 if idx == n - 1 else min(paths, default=float('inf'))
            for i in range(1, nums[idx] + 1):
                paths.append(topdown(idx + i) + 1)
            return min(paths, default=float('inf'))

        ans = topdown(0)
        return ans if ans != float('inf') else -1
