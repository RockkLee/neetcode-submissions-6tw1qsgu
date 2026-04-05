class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # get the peak ele
        last = len(nums) - 1
        l, r = 0, last
        peak_idx = 0
        if last <= 1:
            try:
                return nums.index(target)
            except ValueError:
                return -1
        else:
            while l <= r:
                mid = (l + r) // 2
                peak_idx = mid

                if (mid == last and nums[mid] > nums[mid - 1]) or (mid == 0 and nums[mid] > nums[mid + 1]):
                    break
                if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                    break
                elif nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        if target > nums[peak_idx]:
            return -1
        if target == nums[peak_idx]:
            return peak_idx

        if peak_idx == last:
            l, r = 0, last
        # elif peak_idx == 0:
        #     l, r = peak_idx + 1, last
        elif target < nums[0]:
            l, r = peak_idx + 1, last
        else:
            l, r = 0, peak_idx
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1
