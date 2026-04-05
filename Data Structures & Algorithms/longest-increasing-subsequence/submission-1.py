class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] = length of LIS ending at index i
        dp = [1] * n  # every element alone is an LIS of length 1

        for cur_idx in range(n):
            for i in range(cur_idx):
                if nums[i] < nums[cur_idx]:
                    dp[cur_idx] = max(1 + dp[i], dp[cur_idx])

        return max(dp)
