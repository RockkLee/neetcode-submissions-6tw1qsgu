class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # either rob i → go to i+2, or
        # skip i → go to i+1.
        # @lru_cache
        # def topdown(idx: int) -> int:
        #     if idx > len(nums) - 1:
        #         return 0
        #     return max(nums[idx] + topdown(idx + 2), topdown(idx + 1))

        # return topdown(0)

        # bottom up
        bottomup = [0] * len(nums)
        bottomup[0] = nums[0]
        bottomup[1] = max(nums[0], nums[1])
        for idx in range(2, len(bottomup)):
            bottomup[idx] = max(bottomup[idx - 2] + nums[idx], bottomup[idx - 1])
        return bottomup[-1]
