class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product = 1
        zero_idx = -1
        for idx, num in enumerate(nums):
            if num == 0:
                zero_cnt += 1
                zero_idx = idx
                if zero_cnt > 1:
                    return [0] * len(nums)
            else:
                product *= num

        if zero_cnt == 1:
            res = [0] * len(nums)
            res[zero_idx] = product
            return res
        
        res = []
        for num in nums:
            res.append(int(product / num))
        return res


