class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        best = 0

        for num in s:
            if num - 1 not in s:  # num - 1 not exists -> num = the start of a sequence
                length = 1
                x = num
                while x + 1 in s:
                    x += 1
                    length += 1
                best = max(best, length)

        return best
