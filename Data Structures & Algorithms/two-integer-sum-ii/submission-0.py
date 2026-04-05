class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            add = nums[left] + nums[right]
            if add == target:
                return [left+1, right+1]
            elif add > target:
                right -= 1
            else:
                left += 1
        