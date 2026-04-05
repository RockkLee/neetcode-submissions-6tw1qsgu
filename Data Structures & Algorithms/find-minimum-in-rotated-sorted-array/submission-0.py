class Solution:
    def findMin(self, nums: List[int]) -> int:
       l, r = 0, len(nums) - 1
       while l <= r:
           mid = (l + r) // 2
           if nums[mid] < nums[mid - 1]:
               return nums[mid]
           elif nums[mid] < nums[-1]:
               r = mid - 1
           else:  # nums[mid] > nums[-1] (the equal condition must not exist since all nums are unique)
               l = mid + 1
       return nums[0]
