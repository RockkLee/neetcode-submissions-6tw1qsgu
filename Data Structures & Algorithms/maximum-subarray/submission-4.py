class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, float('-inf')
        idx = 0
        for i in range(idx, len(nums)):
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
            if cur_sum < 0:
                cur_sum = 0

        return max_sum