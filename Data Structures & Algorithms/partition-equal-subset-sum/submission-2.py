from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        lenn = len(nums)
        if sum(nums) %2 == 1:
            return False
        
        @cache
        def dfs(i: int, target: int) -> bool:
            if i >= lenn:
                return target == 0
            if target < 0:
                return False
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        return dfs(0, sum(nums) // 2)
