class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic: dict[int,int] = dict()
        for idx, num in enumerate(nums):
            dic[num] = idx
        
        for idx, num in enumerate(nums):
            val = target - num
            if val in dic and dic[val] != idx:
                return [idx, dic[val]]
        return []