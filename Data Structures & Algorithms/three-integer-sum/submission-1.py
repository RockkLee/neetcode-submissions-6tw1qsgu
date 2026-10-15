class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        last = len(nums) - 1
        nums.sort()

        def twosum(l: int, r: int, target: int):
            while l < r:
                summ = nums[l] + nums[r] + target
                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        for i, n in enumerate(nums):
            if n > 0:
                break
            n = nums[i]
            if i > 0 and nums[i - 1] == n:
                continue
            twosum(i + 1, last, n)
        return res
