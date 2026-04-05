class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        3 <= nums.length <= 3000
        """
        dup: set[Tuple] = set()
        output: list[list[int]] = []
        length = len(nums)
        nums.sort()
        for i in range(length - 2):
            l, r = i + 1, length - 1
            while l < r:
                threesum = nums[l] + nums[r] + nums[i]
                if threesum == 0:
                    if (nums[i], nums[l], nums[r]) not in dup:
                        output.append([nums[i], nums[l], nums[r]])
                        dup.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif threesum > 0:
                    r -= 1
                else:  # threesum < 0
                    l += 1
        return output