class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        sol: List[int] = []

        def backtracking(idx: int):
            # base case
            if idx == len(nums):
                res.append(sol[:])
                return

            # make decisions
            # not take it
            backtracking(idx + 1)
            # take it
            sol.append(nums[idx])
            backtracking(idx + 1)

            # undo decisions
            sol.pop()
        backtracking(0)

        return res