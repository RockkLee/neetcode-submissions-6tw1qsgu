# 4 5 6 7 8 9 0 1 2 3
# 0 1 2 3 4 5 6 7 8 9
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenn = len(nums)
        if lenn == 1:
            return nums[0]
        if lenn == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        l, r = 0, lenn - 1
        while l <= r:
            mid = int((l + r) / 2)
            if nums[mid - 1] > nums[mid] < nums[(mid + 1) % lenn]:
                return nums[mid]
            elif nums[0] <= nums[mid] >= nums[lenn - 1]:
                l = mid + 1
                continue
            else: # nums[0] > nums[mid] < nums[lenn - 1]
                r = mid - 1
                continue
        return -1

