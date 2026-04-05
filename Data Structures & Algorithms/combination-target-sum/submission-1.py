class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output: List[List[int]] = []
        path: List[int] = []

        def backtracking(i: int):
            summ = sum(path)
            # base condition
            if i == len(nums) or summ >= target:
                if sum(path) == target:
                    output.append(path[:])
                return
            # make decisions
            path.append(nums[i])
            backtracking(i)
            path.pop()  # undo the decision
            backtracking(i + 1)

        backtracking(0)
        return output
