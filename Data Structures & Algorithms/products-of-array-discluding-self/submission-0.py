class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        try:
            _1st_zero_pos = nums.index(0)
        except ValueError:
            _1st_zero_pos = -1

        if _1st_zero_pos >= 0:
            # if there are two `0` in the list
            try:
                _2nd_zero_pos = nums.index(0, _1st_zero_pos + 1)
            except ValueError:
                _2nd_zero_pos = -1
            if _2nd_zero_pos >= 0:
                return [0 for _ in range(0, len(nums))]

            # if there is only one `0` in the list
            product = 1
            for idx, num in enumerate(nums):
                if idx != _1st_zero_pos:
                    product *= num
            res = []
            for num in nums:
                if num == 0:
                    res.append(int(product))
                else:
                    res.append(0)
            return res

        # no `0`
        product = 1
        for num in nums:
            product *= num
        return [int(product / num) for num in nums]
