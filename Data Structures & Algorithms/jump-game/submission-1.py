from functools import lru_cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums) - 1

        @lru_cache(None)
        def graph(idx: int) -> bool:
            if idx == 0:
                return True
            for i in range(0, idx):
                if i + nums[i] >= idx:
                    if graph(i):
                        return True
            return False

        return graph(idx)