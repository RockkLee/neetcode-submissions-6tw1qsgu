class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sum = 0
        sol: List[int] = []
        res: List[List[int]] = []

        def backtracking(idx):
            nonlocal sum
            # base case
            if sum >= target:
                if sum == target: res.append(sol[:])
                return

            sum += candidates[idx]
            sol.append(candidates[idx])
            
            # make decisions
            backtracking(idx)  # keep the same num
            # undo the decision
            if sol: sum -= sol.pop()
            if idx + 1 < len(candidates):
                backtracking(idx + 1)  # move to the next num

        backtracking(0)
        return res