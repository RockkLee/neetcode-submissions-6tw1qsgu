class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sum = 0
        sol: List[int] = []
        res: List[List[int]] = []
        candidates.sort()

        def backtracking(start: int):
            nonlocal sum
            # base case
            if sum > target:
                return
            if sum == target:
                res.append(sol[:])
                return

            # make decisions
            for idx in range(start, len(candidates)):  # explores all possible candidates
                if idx > start and candidates[idx] == candidates[idx - 1]:  # skip duplicates
                    continue
                if candidates[idx] > target:
                    break
                sum += candidates[idx]
                sol.append(candidates[idx])
                backtracking(idx + 1)
                # undo the decision
                sum -= sol.pop()

        backtracking(0)
        return res
