class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        sol: List[int] = []
        nums.sort()
        def backtracking(idx: int):
            # base case
            if idx == len(nums):
                res.append(sol[:])
                return

            # make decisions: take it
            sol.append(nums[idx])
            backtracking(idx + 1)
            # undo decisions
            sol.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            # make decisions: not take it
            backtracking(idx + 1)

        backtracking(0)

        return res